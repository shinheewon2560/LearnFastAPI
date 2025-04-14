<script>
    let question_list = []

    function get_question_list() {
        fetch("http://127.0.0.1:8000/fastapi/question/list").then((response) => {
            response.json().then((json) => {
                question_list = json
            })
        })
    }

    get_question_list()
</script>

<ul>
    {#each question_list as question}
        <h1>제목: {question.subject}</h1>
    {/each}
    {#each question_list as question}
        <li>본문: {question.content}</li>
    {/each}
</ul>