var i=0, text;
text ="Hey! I'm EIR. Your Paramedic. Press the SOS Button to for immediate help!!!"
function typing(){
if(i<text.length){
  document.getElementById("text").innerHTML += text.charAt(i);
  i++;
  setTimeout(typing,100);
}
}
typing();