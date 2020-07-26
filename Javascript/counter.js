let counter = 0;
function count(){
    counter+=1;
    //alert(counter)
    if(counter % 10===0){
        //console.log(counter)
        alert(`Count is now ${counter}`)
    }

    document.querySelector('h2').innerHTML=counter
}
document.addEventListener('DOMContentLoaded',()=>{
    //document.querySelector('button').onclick=count;        
    document.querySelector('button').addEventListener("click",count);        
    
})
