// Check All
function check(checked = true) {
  const cbs = document.querySelectorAll('input[name="tasks"]');
  cbs.forEach((cb) => {
    cb.checked = checked;
  });
}
function checkAll(e) {
  e.preventDefault();
  check();
  // reassign click event handler
  this.onclick = uncheckAll;
}
function uncheckAll(e) {
  e.preventDefault();
  check(false);
  // reassign click event handler
  this.onclick = checkAll;
}

const btn = document.querySelector("#checkBtn");
btn.onclick = checkAll;

// Get input from the form and add to the table
let addUser = (e) => {
  let pname = document.getElementById("pname").value;
  let desc = document.getElementById("descr").value;
  let ptasks = document.getElementById("ptasks").value;
  if(!(pname.length && desc.length && ptasks.length)){
    e.preventDefault();
    alert("Incomplete Project form!");
  }
};

let addProject = (e) => {
  let name = document.getElementById("name").value;
  let age = parseInt(document.getElementById("age").value);
  let checkboxes = document.querySelectorAll('input[name="tasks"]:checked');
  let tasks = [];
  checkboxes.forEach((checkbox) => {
    tasks.push(checkbox.value);
  });
  if(!(name.length && age && tasks.length)){
    e.preventDefault();
    alert("Incomplete User form!");
  }
};

document.getElementById("s").addEventListener("click", addUser);

document.getElementById("p").addEventListener("click", addProject);
