let users = [
];
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

// Delete User
let deleteUser = (index) => {
  users.splice(index, 1);
  console.log(`element deleted at index${index}`);
  printData();
};

// Print data to the table
// let printData = () => {
//   document.getElementById("data").innerHTML = "";
//   let i = 0;
//   users.map((x) => {
//     document.getElementById("data").innerHTML += `
//         <tr>
//         <td >${i + 1}</td>
//         <td >${x.name}</td>
//         <td >${x.age}</td>
//         <td >${x.gender}</td>
//         <td >${x.tasks}</td>
//         <td > <button class="btn btn-outline-danger btn-sm" onClick="deleteUser(${i})"><i class="bi bi-trash"></i></button> </td>
//         </tr>
//         `;
//     i += 1;
//   });
  // console.log("printdata");
// };
printData();

// Get input from the form and add to the table
let addData = (e) => {
  // e.preventDefault();
  console.log("Added data");
  let name = document.getElementById("name").value;
  let age = parseInt(document.getElementById("age").value);
  let radiobts = document.querySelectorAll('input[name="gender"]');
  let checkboxes = document.querySelectorAll('input[name="tasks"]:checked');
  let tasks = [];
  let gender;
  for (let rbt of radiobts) {
    if (rbt.checked) {
      gender = rbt.value;
      //   console.log(gender)
      break;
    }
  }
  checkboxes.forEach((checkbox) => {
    tasks.push(checkbox.value);
  });
  console.log(tasks);
  let dataToAdd = {
    name,
    age,
    gender,
    tasks,
  };
  if (name.length && age && tasks.length > 0) {
    users.push(dataToAdd);
  } else {
    alert("Something is missing");
  }
  document.getElementById("userDetails").reset();
  printData();
};

// document.getElementById("s").addEventListener("click", addData);
