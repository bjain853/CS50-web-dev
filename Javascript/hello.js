// function hello() {
//     const currentHeading = document.querySelector('h1');
//     if (currentHeading.innerHTML === "Hello") {
//         currentHeading.innerHTML = "Goodbye"

//     } else {
//         currentHeading.innerHTML = "Hello"

//     }
// }

document.addEventListener('DOMContentLoaded',()=>{
        document.querySelector('form').onsubmit=()=>{
          const name =  document.querySelector('#name').value;
          alert(`Hello ,${name}!`);
        }
})