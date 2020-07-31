
if (!localStorage.getItem('counter')){
    localStorage.setItem('counter',0);
}
//let counter = 0; 
function count() {
    let counter = localStorage.getItem('counter');
    counter ++;
    //alert(counter)
    // if(counter % 10===0){
    //     //console.log(counter)
    //     alert(`Count is now ${counter}`)
    // }
    document.querySelector('h2').innerHTML = counter
    localStorage.setItem('counter',counter);
}



document.addEventListener('DOMContentLoaded', () => {
    //document.querySelector('button').onclick=count;        
    //const id = setInterval(count, 1000);

    document.querySelector('h2').innerHTML= localStorage.getItem('counter');
    // document.querySelector('button').addEventListener('click', () => {
       
    //     //clearInterval(id);
    //     count();
    // }
    // )
    document.querySelector('button').onclick=count;


});
