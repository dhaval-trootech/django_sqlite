let btn = document.getElementById("my-btn") ;
let myTable = document.querySelector("#my-table");

function toggleData() {
    console.log("Class Right Now: ", myTable.style.display)
  if (myTable.style.display === "none") {
    myTable.style.display = "block";
  } else {
    myTable.style.display = "none";
  }
}

btn.addEventListener("click", toggleData) ;
