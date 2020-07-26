document.querySelector('#red').onclick = () =>{
           changeColor('red');
        }
        document.querySelector('#blue').onclick = () =>{
           changeColor('blue');
        }
        document.querySelector('#green').onclick = () =>{
           changeColor('green');
        }

        const buttons = document.querySelectorAll("button");
        buttons.forEach((button) => {
          button.onclick = () => {
            document.querySelector("#hello").style.color = button.dataset.color;
          };
        });


