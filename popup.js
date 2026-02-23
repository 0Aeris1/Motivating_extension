document.addEventListener("DOMContentLoaded", () => {
    const go = document.getElementById("go");
    const inputEl = document.getElementById("input");
    const outputEl = document.getElementById("output");

async function runMotivation() {
    const input = inputEl.value || "";

    // Clear input immediately
    inputEl.value = "";

    try {
            const response = await fetch("http://127.0.0.1:8000/motivate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: input })
        });
 
            const data = await response.json();

        if (response.ok) {
            // Normal AI Output
            msg = data.response

        } else {
            // rate-limit or other errors
            msg = data.detail || "AI died from an uknown error";

        }
            typeWriter(outputEl, msg + "\n\n" + getAsciiArt(), 80); 

        } catch (err) {

            typeWriter(outputEl, "Engine offline.\n" + err, 80);

        }
    }
    // 1️⃣ Attach handler
    go.addEventListener("click", runMotivation);

    // 2️⃣ Auto-run once on open
    runMotivation();

});

function typeWriter(element, text, delay = 80) {
    element.textContent = ""; // clear existing
    const words = text.split(" ");
    let i = 0;

    const interval = setInterval(() => {
        element.textContent += (i === 0 ? "" : " ") + words[i];
        i++;
        if (i >= words.length) clearInterval(interval);
    }, delay);

}

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


