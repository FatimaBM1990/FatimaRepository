let age = 0;
let money = 1000;
let happiness = 50;
let bmi = 25;
let iq = 100;
function startGame() {
    document.getElementById('start-screen').style.display = 'none';
    document.getElementById('game-container').style.display = 'block';
    updateStats();
}

function updateStats() {
    document.getElementById('age').textContent = age;
    document.getElementById('money').textContent = money;
    document.getElementById('happiness').textContent = happiness;
    document.getElementById('bmi').textContent = bmi;
    document.getElementById('iq').textContent = iq;
    updateImage();
    checkUnlocks();
}

function ageUp() {
    age++;
    if (age % 2 === 0) happiness = Math.max(happiness - 5, 0);
    if (age === 11) { startYear6Quiz(); } 
    if (age === 16) { startYear11Quiz(); } 
    updateStats();
    checkGameOver();
}

function updateImage() {
    let stage;
    if (age <= 2) stage = 'baby';
    else if (age <= 5) stage = 'toddler';
    else if (age <= 10) stage = 'kid';
    else if (age <= 18) stage = 'teen';
    else if (age <= 60) stage = 'adult';
    else stage = 'grandpa';
    document.getElementById('character-image').src = images[stage];
}

function checkUnlocks() {
    if (age >= 18) {
        document.getElementById('gamble-button').style.display = 'inline-block';
        document.getElementById('university-button').style.display = 'inline-block';
    }
}

function goShopping() {
    document.getElementById('shopping-container').style.display = 'block';
}

function enterShop(shopName) {
    
    alert("Entering " + shopName);
    document.getElementById('shopping-container').style.display = 'none';
}

function exercise() {
    if (bmi > 18) {
        bmi = Math.max(bmi - 1, 18);
        happiness = Math.min(happiness + 10, 100);
        updateStats();
    } else {
        alert("BMI is already low!");
    }
}

function readBooks() {
    iq = Math.min(iq + 5, 200);
    updateStats();
}

function investInEducation() {
    if (money >= 100) {
        money -= 100;
        iq = Math.min(iq + 10, 200);
        alert("You invested in education! IQ increased.");
        updateStats();
    } else {
        alert("Not enough money!");
    }
}

function gamble() {
    let bet = prompt("Enter your bet amount:");
    bet = parseInt(bet);
    if (bet > 0 && bet <= money) {
        let win = Math.random() < 0.5;
        if (win) {
            money += bet;
            displayConfetti();
            alert("You won! Your money increased by $" + bet);
        } else {
            money -= bet;
            alert("You lost! Your money decreased by $" + bet);
        }
        updateStats();
    } else {
        alert("Invalid bet or not enough money!");
    }
}

function displayConfetti() {
    const confetti = document.getElementById('confetti');
    confetti.style.display = 'block';
    setTimeout(() => confetti.style.display = 'none', 1000);
}

function chooseUniversity() {
    const fields = ['Science', 'Arts', 'Commerce', 'Engineering'];
    let choice = prompt("Choose a field of study: Science, Arts, Commerce, Engineering", "Science");
    if (fields.includes(choice)) {
        alert("You chose " + choice + ". Good luck in your studies!");
        money -= 500;
        iq += 20;
        updateStats();
    } else {
        alert("Invalid choice");
    }
}

function startYear6Quiz() {
    
    alert("Starting Year 6 SATs Quiz...");
    
    let questions = [
        { q: "5 + 3", a: "8" },
        { q: "10 - 2", a: "8" }
    ];
    questions.forEach((question) => {
        let answer = prompt(question.q);
        if (answer !== question.a) {
            happiness -= 5;
        }
    });
    updateStats();
}

function startYear11Quiz() {
    
    alert("Starting Year 11 GCSEs Quiz...");
 
    let questions = [
        { q: "12 x 12", a: "144" },
        { q: "25 / 5", a: "5" }
    ];
    questions.forEach((question) => {
        let answer = prompt(question.q);
        if (answer !== question.a) {
            happiness -= 5;
        }
    });
    updateStats();
}

function checkGameOver() {
    if (happiness === 0) {
        alert("The character is too unhappy! Game over.");
    }
}

document.getElementById('character-image').onclick = () => {
    ageUp();
};
