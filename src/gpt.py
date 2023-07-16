import os
import requests
import json
try:
    import src.util.data as data
except:
    import util.data as data


class Completion:
    @staticmethod
    def create(prompt, option='answer'):
        try:
            resp = ""
            content = data.prompts[option]
            endpoint = "https://ava-ai-ef611.web.app/"
            prompt_chunks = [prompt[i:i+500] for i in range(0, len(prompt), 500)]
            
            for chunk in prompt_chunks:
                with requests.post(
                    endpoint,
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(
                        {
                            "model": "gpt-4",
                            "temperature": 0.7,
                            "messages": [
                                {
                                    "role": "system",
                                    "content": content,
                                },
                                {"role": "user", "content": chunk},
                            ],
                        }
                    ),
                    stream=True,
                ) as resp_obj:
                    resp_obj.raise_for_status()
                    for line in resp_obj.iter_lines():
                        line_text = line.decode("utf-8").strip()
                        if line_text.startswith("data:"):
                            data = line_text[len("data:"):]
                            try:
                                data_json = json.loads(data)
                                if "choices" in data_json:
                                    choices = data_json["choices"]
                                    for choice in choices:
                                        if "finish_reason" in choice and choice["finish_reason"] == "stop":
                                            break
                                        if "delta" in choice and "content" in choice["delta"]:
                                            resp += choice["delta"]["content"]
                            except json.JSONDecodeError:
                                pass
        except requests.exceptions.RequestException as e:
            raise Exception("Unable to fetch the response.") from e
        
        return resp