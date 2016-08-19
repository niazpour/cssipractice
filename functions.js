function timestwo(a){
    return (a*2);
}
function timessix(a){
    return a * (timestwo(2) + 2);
}
function roll(){
  return Math.floor(Math.random()*6)+1;
}
function mouse(){
var text = "ELEPHANTBEARMOUSECOW"
text1 = text.substring(0,12);
text2 = text.substring(17,20);
text3= text.substring(12,17).toLowerCase();
text = (text1 + text3 + text2);
return text;
}
function capitalize(){
  var word = "foo";
  word2 = word.substring(0,1).toUpperCase()+ word.substring(1,3);
  return word2;
}
function endcapitalize(){
  var word = "foo";
  word2 = word.substring(0,2) + word.substring(2,3).toUpperCase();
  return word2;
}
function skeeter(a){
  var skeeterRater = (a)
  if (skeeterRater >= 450) {
    window.alert('Inconceivable!');
} else if (450 > skeeterRater && skeeterRater > 350) {
    window.alert('Great');
} else if (250 > skeeterRater && skeeterRater > 150){
    window.alert('Decent');
} else{
    window.alert('Pretty bad');
}
}
var students = ['Alanah', 'Vernon','Juliette', 'Adolfo']
function chopAndFlip(array) {
  var middle = array.length / 2;
  var secondHalf =
  array.splice(middle,array.length);
  return secondHalf.concat(array);
}
var movies = ["Thor","Spy","Now You See Me", "Les Miserables"]
function myFavorites(movies){
  for(var i=0; i < movies.length; i =i+1){
  alert(movies[i]+"? That's my fave!")
  }
}
//while loop
var i=1;
  while(i<10){
    console.log(i);
    i =i+1;
}
//for loop
for (var i=1; i<10;i=i+1){
  console.log(i);
}
function reverse(arr){
  var temp = [];
  var a =0
  for (var i= arr.length -1;i>=0;i--){
    temp[a]= arr[i];
    a++;
  }
  arr=temp;
  console.log(arr);
}
