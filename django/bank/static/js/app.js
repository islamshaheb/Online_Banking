 function name()
 {
    var name=document.forms["main"]["name"];

     if (name.value == "")
    {
        window.alert("Please enter your name.");
        document.write("okkkkkkkkkkkkkkkkkkkk");
        name.focus();
        return false;
    }
 }
