function display(){
    let email=document.getElementById('email').value.trim();
    let password=document.getElementById('password').value.trim();
    var pass=password;
    let check=document.getElementById('remember').checked;

    let uwarn=document.getElementById('uerrormsg');
    let pwarn=document.getElementById('perrormsg');
    let cwarn=document.getElementById('cerrormsg');
    // let email="helo";
    // pwarn.classList.add("errormsg");
    // console.log(email);


    if(email===""){
        console.log("email can not be empty.");
        document.getElementById('ufail').style.visibility="visible";
        // document.getElementById('uerrormsg').innerHTML="email can not be empty...!";
        uwarn.classList.add("errormsg");
        document.getElementById("email").classList.add("error");



    }else
     if(email!='abcd9821@gmail.com'){
        console.log("Please enter an right email.");
        // document.getElementById('email').reset();
        uwarn.classList.add("errormsg");
        document.getElementById('ufail').style.visibility="visible";
        document.getElementById("email").classList.add("error");

    }else if(password!='1234'){
        console.log("Please enter an right password.");
        pwarn.classList.add("errormsg");
        uwarn.classList.remove("errormsg");
        document.getElementById('ufail').style.visibility="hidden";
        document.getElementById('usuccess').style.visibility="visible";
        document.getElementById('pfail').style.visibility="visible";
        document.getElementById("password").classList.remove("error");
        document.getElementById("email").classList.remove("error");
        document.getElementById("email").classList.add("success");
        paasscount(pass);
    }

   
    else {
        console.log('succefully login');
        document.getElementById('usuccess').style.visibility="hidden";
        document.getElementById('ufail').style.visibility="hidden";


        document.getElementById('psuccess').style.visibility="hidden";
        document.getElementById('pfail').style.visibility="hidden";
        document.getElementById('remember').checked=false;
        pwarn.classList.remove("errormsg");
        document.getElementById('pfail').style.visibility="hidden";
        document.getElementById("email").classList.remove("error");
        uwarn.classList.remove("errormsg");
        document.getElementById('ufail').style.visibility="hidden";
        document.getElementById("email").classList.remove("error");




        pwarn.classList.remove("errormsg");
        uwarn.classList.remove("errormsg");
        paasscount(pass);
        


        let email=document.getElementById('email').value="";
        let password=document.getElementById('password').value="";

    }
    function paasscount(pas){
        pas.this=pass;
        // console.log()
        var spe=0;
        var num=0;
        var char=0
        for(var i=0;i<pas.length;i++){
            // console.log(pas[i]);
            if(pas[i]==0||pas[i]==1||pas[i]==2||pas[i]==3||pas[i]==4||pas[i]==5||pas[i]==6||pas[i]==7||pas[i]==8||pas[i]==9){
                num=num+1;
            }else
            if(pas[i]=='@'||pas[i]=='#'||pas[i]=='%'||pas[i]=='_'||pas[i]=='/'||pas[i]=='!'||pas[i]=='$'){
                spe=spe+1;
            }else{
                char=char+1;

            }

        }
        console.log("number",num)
        console.log("special",spe)
        console.log("char",char)
        console.log(pas.length);



    }
   


    

}