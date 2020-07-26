document.addEventListener('DOMContentLoaded', () => {
    //BY default submit is disabled
    document.querySelector('#submit').disabled = true;

    document.querySelector('#task').onkeyup = () => {
        if (document.querySelector('#task').value.length > 0) {
            //console.log('typed something and didnt delete');
            document.querySelector('#submit').disabled = false;

        } else {
            document.querySelector('#submit').disabled = true;

        }

    }
    document.querySelector('form').onsubmit = () => {
        const task = document.querySelector('#task').value;
        //console.log(task);
        const li = document.createElement('li');
        li.innerHTML = task;
        document.querySelector('#tasks_list').append(li);
        document.querySelector('#task').value = '';
        document.querySelector('#submit').disabled = true;

        // stop form from submitting
        return false;
    }
})