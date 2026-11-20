/* Extracted page script for tests/Kiem_Tra_Marugoto_L6_7_8.html */
const answers = {
    q1: 'B', q2: 'C', q3: 'B', q4: 'D', q5: 'C',
    q6: 'B', q7: 'C', q8: 'B', q9: 'B', q10: 'C'
};

function gradeTest() {
    let score = 0;
    let total = 10;

    for (let i = 1; i <= total; i++) {
        let qName = 'q' + i;
        let options = document.getElementsByName(qName);
        let selectedValue = null;
        let selectedLabel = null;
        let correctLabel = null;

        for (let opt of options) {
            // Find label of the correct option
            if (opt.value === answers[qName]) {
                correctLabel = opt.parentElement;
            }
            // Find selected option
            if (opt.checked) {
                selectedValue = opt.value;
                selectedLabel = opt.parentElement;
            }
        }

        // Reset classes
        for (let opt of options) {
            opt.parentElement.classList.remove('correct-opt', 'wrong-opt');
        }

        if (selectedValue === answers[qName]) {
            score++;
            if (selectedLabel) selectedLabel.classList.add('correct-opt');
        } else {
            if (selectedLabel) selectedLabel.classList.add('wrong-opt');
            if (correctLabel) correctLabel.classList.add('correct-opt'); // Highlight correct answer
        }

        // Show feedback
        document.getElementById('fb' + i).style.display = 'block';
    }

    // Show result box
    let resultBox = document.getElementById('finalResult');
    resultBox.style.display = 'block';

    let scorePercent = score / total * 5; // MCQ is 5 points
    resultBox.innerHTML = `Bạn làm đúng ${score}/${total} câu trắc nghiệm!<br> Điểm phần trắc nghiệm: ${scorePercent}/5 điểm`;

    if (score >= 8) {
        resultBox.style.color = '#27ae60';
        resultBox.style.borderColor = '#27ae60';
        resultBox.style.backgroundColor = '#e8f8f5';
    } else if (score >= 5) {
        resultBox.style.color = '#f39c12';
        resultBox.style.borderColor = '#f39c12';
        resultBox.style.backgroundColor = '#fef9e7';
    } else {
        resultBox.style.color = '#c0392b';
        resultBox.style.borderColor = '#c0392b';
        resultBox.style.backgroundColor = '#fadbd8';
    }

    // Show suggested answers for essay
    let saElements = document.getElementsByClassName('sa-show');
    for(let el of saElements) {
        el.style.display = 'block';
    }

    // Scroll to results
    resultBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
}
