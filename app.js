function submitQuestion() {
    const context = document.getElementById('context').value;
    const question = document.getElementById('question').value;

    const data = { context: context, question: question };

    fetch('http://127.0.0.1:8000/ask/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('answer').innerText = 'Answer: ' + data.answer;
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('answer').innerText = 'Error processing your question.';
    });
}
