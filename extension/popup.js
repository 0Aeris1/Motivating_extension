document.addEventListener("DOMContentLoaded", () => {
    const go = document.getElementById("go");
    const inputEl = document.getElementById("input");
    const outputEl = document.getElementById("output");

// Function to call backend and display AI motivational message
async function runMotivation() {
    const input = inputEl.value || ""; // Use input or default
    inputEl.value = ""; // Clear input immediately

    try {
            // Send request to backend API (change this for local hosting)
            const response = await fetch("https://motivating-extension.onrender.com/motivate", {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify({ text: input })
        });
 
            const data = await response.json();

        if (response.ok) {
            msg = data.response // Normal AI output
        } else {
            msg = data.detail || "AI died from an uknown error"; // Rate-limit or other errors
        }
            // Display message with typing effect + ASCII art
            typeWriter(outputEl, msg + "\n\n" + getAsciiArt(), 80); 

        } catch (err) {
            typeWriter(outputEl, "Engine offline.\n" + err, 80);

        }
    }

    go.addEventListener("click", runMotivation); // Attach click handler
    runMotivation(); // Auto-run once on extension open

});

// Typewriter effect: prints words one by one
function typeWriter(element, text, delay = 80) {
    element.textContent = ""; // Clear existing content
    const words = text.split(" ");
    let i = 0;

    const interval = setInterval(() => {
        element.textContent += (i === 0 ? "" : " ") + words[i];
        i++;
        if (i >= words.length) clearInterval(interval);
    }, delay);

}

// Random motivational ASCII art
function getAsciiArt() {
    const arts = [
    `  (ง'̀-'́)ง
    FIGHT.`,

    `  ┌( ಠ_ಠ)┘
    MOVE.`,

    `  (•̀o•́)ง
    START.`,

    `  >_>
    DO IT.`,

    `  (¬‿¬)
    YEAH!`,

    `  (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
    GO GO!`,

    `  (ง •̀_•́)ง
      PUSH!`,

    `  (☞ﾟヮﾟ)☞
      YOU GOT THIS!`,

    `  (ಠ_ಠ)
      FOCUS!`,

    `  (•_•)
      NO EXCUSES!`,

    `  (⊙_⊙)
      KEEP GOING!`,

    `  (⌐■_■)
      WORK!`,

    `  (╭☞ ͡° ͜ʖ ͡°)╭☞
      SMILE & WORK!`,

    `  (ﾉಥ益ಥ）ﾉ
      GRIND!`,

    `  (✧ω✧)
      HUSTLE!`,

    `  ( •_•)>⌐■-■
      MOTIVATE!`
        ];

    return arts[Math.floor(Math.random() * arts.length)];
}


