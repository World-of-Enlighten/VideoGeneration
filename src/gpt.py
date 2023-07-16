from json import loads, JSONDecodeError
from requests import post, exceptions
try:
    import util.data as data
except:
    import src.util.data as data


class Completion:
    def create(prompt,option='caption'):
        try:
            resp_obj = post(
                "https://ava-alpha-api.codelink.io/api/chat",
                headers={"Content-Type": "application/json"},
                json={
                    "model": "gpt-4",
                    "temperature": 0.6,
                    "stream": True,
                    "messages": [
                        {"role": "system", "content": data.prompts[option]},
                        {"role": "user", "content": prompt},
                    ],
                },
                timeout=30,
            )
        except exceptions.RequestException:
            raise Exception("Unable to fetch the response.")

        resp = ""
        for line in resp_obj.iter_lines():
            line_text = line.decode("utf-8").strip()
            if line_text.startswith("data:"):
                data = line_text.split("data:")[1]
                try:
                    data_json = loads(data)
                    if "choices" in data_json:
                        choices = data_json["choices"]
                        for choice in choices:
                            if (
                                "finish_reason" in choice
                                and choice["finish_reason"] == "stop"
                            ):
                                break
                            if "delta" in choice and "content" in choice["delta"]:
                                resp += choice["delta"]["content"]
                except JSONDecodeError:
                    pass
        return resp
