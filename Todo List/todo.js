function updateList(){
    var c=this.id.replace("c","");
    var item=document.getElementById("s"+c);
    if (this.checked){
      item.className="checked";
    }
    else{
        item.className="";
    }
}

function addItem(List,item){
    totalItems++;
    var Listitem=document.createElement("li");
    var cb=document.createElement("input");
    cb.type="checkbox";
    cb.id="c"+totalItems;
    cb.onclick=updateList;
    var span=document.createElement("span");
    span.innerText=item;
    span.id="s"+totalItems;
    Listitem.appendChild(cb);
    Listitem.appendChild(span);
    List.appendChild(Listitem);
}
var enteredText=document.getElementById("newItem");
enteredText.focus();
var totalItems=0;
var btnAdd=document.getElementById("add");
btnAdd.onclick=function()
{
    var itemText=enteredText.value;
    addItem(document.getElementById("List"),itemText);
};