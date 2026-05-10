const canvas = document.getElementById("goBoard");
const ctx = canvas.getContext("2d");

const blackScoreEl = document.getElementById("blackScore");
const whiteScoreEl = document.getElementById("whiteScore");
const winScoreEl = document.getElementById("winScore");

const messageBox = document.getElementById("messageBox");
const resultBox = document.getElementById("resultBox");

const resetBtn = document.getElementById("resetBtn");
const finishBtn = document.getElementById("finishBtn");

const BOARD_SIZE = 9;
const CELL = 52;
const MARGIN = 42;

const BOARD_PIXELS =
    MARGIN * 2 + CELL * (BOARD_SIZE - 1);

const CLICK_RADIUS = 28;

let currentState = null;

let isThinking = false;

let resultShown = false;

let capturedEffects = [];

canvas.width = BOARD_PIXELS;
canvas.height = BOARD_PIXELS;


async function fetchState() {

    const response = await fetch("/api/state");

    const data = await response.json();

    updateState(data);
}


async function sendMove(x, y) {

    if (isThinking) return;

    if (!currentState) return;

    if (currentState.game_over) return;

    if (currentState.board[x][y] !== ".") return;

    isThinking = true;

    const tempBoard = cloneBoard(currentState.board);

    tempBoard[x][y] = "X";

    drawBoard(tempBoard);

    messageBox.textContent =
        `Bạn vừa đánh tại dòng ${x}, cột ${y}. AI đang suy nghĩ...`;

    const playerResponse = await fetch(
        "/api/player-move",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({ x, y })
        }
    );

    const playerData = await playerResponse.json();

    updateState(playerData);

    if (playerData.game_over) {
        isThinking = false;
        return;
    }

    await sleep(50);

    const aiResponse = await fetch(
        "/api/ai-move",
        {
            method: "POST"
        }
    );

    const aiData = await aiResponse.json();

    updateState(aiData);

    isThinking = false;
}


async function resetGame() {

    isThinking = false;

    resultShown = false;

    const response = await fetch(
        "/api/reset",
        {
            method: "POST"
        }
    );

    const data = await response.json();

    updateState(data);
}


async function finishGame() {

    if (isThinking) return;

    const response = await fetch(
        "/api/finish",
        {
            method: "POST"
        }
    );

    const data = await response.json();

    updateState(data);
}


function updateState(data) {

    currentState = data;

    blackScoreEl.textContent = data.black_score;

    whiteScoreEl.textContent = data.white_score;

    winScoreEl.textContent = data.win_score;

    messageBox.textContent = data.message;

    drawBoard(data.board);

    showResult(data);

    if (data.captured) {
        triggerCaptureEffect(data.captured);
    }
}


function triggerCaptureEffect(captured) {

    for (const [x, y] of captured) {

        capturedEffects.push({
            x,
            y,
            alpha: 1,
            radius: 10
        });
    }
}


function showResult(data) {

    resultBox.className = "result-box hidden";

    resultBox.textContent = "";

    if (!data.game_over) return;

    if (data.result_effect === "win") {

        resultBox.className = "result-box win";

        resultBox.textContent =
            "🎉 BẠN ĐÃ THẮNG AI 🎉";

        if (!resultShown) {

            launchConfetti();

            resultShown = true;
        }
    }

    else if (data.result_effect === "lose") {

        resultBox.className = "result-box lose";

        resultBox.textContent =
            "💀 BẠN ĐÃ THUA AI 💀";

        resultShown = true;
    }

    else {

        resultBox.className = "result-box draw";

        resultBox.textContent =
            "🤝 HÒA 🤝";

        resultShown = true;
    }
}


function cloneBoard(board) {

    return board.map(row => [...row]);
}


function sleep(ms) {

    return new Promise(resolve =>
        setTimeout(resolve, ms)
    );
}


function drawBoard(board) {

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );

    ctx.fillStyle = "#d9a441";

    roundRect(
        ctx,
        0,
        0,
        BOARD_PIXELS,
        BOARD_PIXELS,
        18,
        true,
        false
    );

    ctx.lineWidth = 14;

    ctx.strokeStyle = "#7c4a12";

    roundRect(
        ctx,
        8,
        8,
        BOARD_PIXELS - 16,
        BOARD_PIXELS - 16,
        10,
        false,
        true
    );

    ctx.lineWidth = 2;

    ctx.strokeStyle = "#1f1305";

    for (let i = 0; i < BOARD_SIZE; i++) {

        const pos = MARGIN + i * CELL;

        ctx.beginPath();

        ctx.moveTo(MARGIN, pos);

        ctx.lineTo(
            MARGIN + CELL * (BOARD_SIZE - 1),
            pos
        );

        ctx.stroke();

        ctx.beginPath();

        ctx.moveTo(pos, MARGIN);

        ctx.lineTo(
            pos,
            MARGIN + CELL * (BOARD_SIZE - 1)
        );

        ctx.stroke();
    }

    const starPoints = [
        [2, 2],
        [2, 6],
        [4, 4],
        [6, 2],
        [6, 6]
    ];

    for (const [x, y] of starPoints) {

        drawCircle(
            MARGIN + y * CELL,
            MARGIN + x * CELL,
            4,
            "#1f1305",
            "#1f1305"
        );
    }

    for (let i = 0; i < BOARD_SIZE; i++) {
        for (let j = 0; j < BOARD_SIZE; j++) {

            const cell = board[i][j];

            const cx = MARGIN + j * CELL;

            const cy = MARGIN + i * CELL;

            if (cell === "X") {

                drawStone(
                    cx,
                    cy,
                    "#111111",
                    "#000000"
                );
            }

            else if (cell === "O") {

                drawStone(
                    cx,
                    cy,
                    "#f8fafc",
                    "#9ca3af"
                );
            }
        }
    }

    drawCapturedEffects();
}


function drawCapturedEffects() {

    for (
        let i = capturedEffects.length - 1;
        i >= 0;
        i--
    ) {

        const effect = capturedEffects[i];

        const cx =
            MARGIN + effect.y * CELL;

        const cy =
            MARGIN + effect.x * CELL;

        ctx.beginPath();

        ctx.arc(
            cx,
            cy,
            effect.radius,
            0,
            Math.PI * 2
        );

        ctx.fillStyle =
            `rgba(255, 80, 80, ${effect.alpha})`;

        ctx.fill();

        effect.alpha -= 0.05;

        effect.radius += 1.4;

        if (effect.alpha <= 0) {
            capturedEffects.splice(i, 1);
        }
    }

    requestAnimationFrame(() => {

        if (
            capturedEffects.length > 0
            && currentState
        ) {
            drawBoard(currentState.board);
        }
    });
}


function drawStone(x, y, fill, stroke) {

    ctx.beginPath();

    ctx.arc(
        x,
        y,
        18,
        0,
        Math.PI * 2
    );

    ctx.fillStyle = fill;

    ctx.fill();

    ctx.lineWidth = 2;

    ctx.strokeStyle = stroke;

    ctx.stroke();
}


function drawCircle(x, y, r, fill, stroke) {

    ctx.beginPath();

    ctx.arc(
        x,
        y,
        r,
        0,
        Math.PI * 2
    );

    ctx.fillStyle = fill;

    ctx.fill();

    ctx.strokeStyle = stroke;

    ctx.stroke();
}


function roundRect(
    ctx,
    x,
    y,
    width,
    height,
    radius,
    fill,
    stroke
) {

    ctx.beginPath();

    ctx.moveTo(x + radius, y);

    ctx.lineTo(x + width - radius, y);

    ctx.quadraticCurveTo(
        x + width,
        y,
        x + width,
        y + radius
    );

    ctx.lineTo(
        x + width,
        y + height - radius
    );

    ctx.quadraticCurveTo(
        x + width,
        y + height,
        x + width - radius,
        y + height
    );

    ctx.lineTo(x + radius, y + height);

    ctx.quadraticCurveTo(
        x,
        y + height,
        x,
        y + height - radius
    );

    ctx.lineTo(x, y + radius);

    ctx.quadraticCurveTo(
        x,
        y,
        x + radius,
        y
    );

    ctx.closePath();

    if (fill) ctx.fill();

    if (stroke) ctx.stroke();
}


function getClickedPosition(event) {

    const rect =
        canvas.getBoundingClientRect();

    const scaleX =
        canvas.width / rect.width;

    const scaleY =
        canvas.height / rect.height;

    const clickX =
        (event.clientX - rect.left)
        * scaleX;

    const clickY =
        (event.clientY - rect.top)
        * scaleY;

    let nearestRow = null;

    let nearestCol = null;

    let minDistance = Infinity;

    for (let row = 0; row < BOARD_SIZE; row++) {
        for (let col = 0; col < BOARD_SIZE; col++) {

            const pointX =
                MARGIN + col * CELL;

            const pointY =
                MARGIN + row * CELL;

            const distance = Math.sqrt(
                Math.pow(clickX - pointX, 2)
                +
                Math.pow(clickY - pointY, 2)
            );

            if (distance < minDistance) {

                minDistance = distance;

                nearestRow = row;

                nearestCol = col;
            }
        }
    }

    if (minDistance <= CLICK_RADIUS) {

        return {
            x: nearestRow,
            y: nearestCol
        };
    }

    return null;
}


function launchConfetti() {

    const duration = 900;

    const end =
        Date.now() + duration;

    const colors = [
        "#22c55e",
        "#facc15",
        "#38bdf8",
        "#f97316"
    ];

    function frame() {

        const timeLeft =
            end - Date.now();

        if (timeLeft <= 0) return;

        const confetti =
            document.createElement("div");

        confetti.style.position = "fixed";

        confetti.style.left =
            `${Math.random() * 100}%`;

        confetti.style.top = "-10px";

        confetti.style.width = "8px";

        confetti.style.height = "14px";

        confetti.style.background =
            colors[
                Math.floor(
                    Math.random()
                    * colors.length
                )
            ];

        confetti.style.zIndex = "9999";

        confetti.style.borderRadius = "2px";

        confetti.style.animation =
            "fall 0.9s linear forwards";

        document.body.appendChild(confetti);

        setTimeout(() => {
            confetti.remove();
        }, 1000);

        requestAnimationFrame(frame);
    }

    frame();
}


const style =
    document.createElement("style");

style.textContent = `
@keyframes fall {
    to {
        transform:
            translateY(100vh)
            rotate(360deg);

        opacity: 0;
    }
}
`;

document.head.appendChild(style);


canvas.addEventListener(
    "click",
    function (event) {

        const position =
            getClickedPosition(event);

        if (!position) return;

        sendMove(position.x, position.y);
    }
);


resetBtn.addEventListener(
    "click",
    resetGame
);

finishBtn.addEventListener(
    "click",
    finishGame
);

fetchState();
