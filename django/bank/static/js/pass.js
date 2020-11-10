
//var x=parseInt(prompt("ENter first Number"))
//document.write("kkkkkkkkkkkkkkkkkkkk");
//var name=document.forms["main"]["username"];
//document.write(name);
document.write("                              o");


 function name()
 {
    var name=document.forms.main.username;

     if (name.value == "")
    {
        window.alert("Please enter your name.");
        document.write("okkkkkkkkkkkkkkkkkkkk");
        name.focus();
        return false;
    }
 }
