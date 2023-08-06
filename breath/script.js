const graph = document.getElementById("graph");
    const svg = document.getElementById("sinusoid");
    const frequencyInput = document.getElementById("frequency");
    const amplitudeInput = document.getElementById("amplitude");
    const speedInput = document.getElementById("speed");

    let amplitude = 50;
    let frequency = 0.02;
    let time = 0;
    let speed = 5;
    let animationId = null;

    function drawSinusoidalCurve() {
      const width = graph.clientWidth;
      const height = 200;
      const points = [];

      for (let x = 0; x < width; x++) {
        const y = amplitude * Math.sin(frequency * (x + time));
        points.push(`${x},${height / 2 - y}`);
      }

      const pathString = `M${points.join(" L")}`;
      svg.innerHTML = `<path d="${pathString}" fill="none" stroke="blue" stroke-width="2" />`;

      time += speed;
      animationId = requestAnimationFrame(drawSinusoidalCurve); 
    }

    frequencyInput.addEventListener("input", () => {
      frequency = parseFloat(frequencyInput.value);
    });

    amplitudeInput.addEventListener("input", () => {
      amplitude = parseInt(amplitudeInput.value);
    });

    speedInput.addEventListener("input", () => {
      speed = parseInt(speedInput.value);
    });

drawSinusoidalCurve();