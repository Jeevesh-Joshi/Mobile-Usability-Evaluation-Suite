let users = [
  {
    id: 1,
    name: "Maneesh",
    age: 21,
    gender: " Male",
    tasks: ["1. login"],
  },
  {
    id: 2,
    name: "Gupta",
    age: 22,
    gender: " Male",
    tasks: ["1. login"],
  },
  {
    id: 3,
    name: "alexa",
    age: 29,
    gender: " Female",
    tasks: ["1. login"],
  },
];

let printData = () => {
  document.getElementById("data").innerHTML = "";
  let i = 0;
  users.map((x) => {
    
    document.getElementById("data").innerHTML += `
        <tr>
        <td >${i + 1}</td>
        <td >${x.name}</td>
        <td >${x.age}</td>
        <td >${x.gender}</td>
        <td >${x.tasks}</td>
        </tr>
        `;
    i += 1;
  });
  // console.log("printdata");
};
printData();

let addData = (e) => {
  e.preventDefault();
  console.log("Add data");
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
  console.log(tasks)
  let dataToAdd = {
    name,
    age,
    gender,
    tasks,
  };
  if (name.length && age && tasks.length > 0) {
    users.unshift(dataToAdd);
  } else {
    alert("Something is missing");
  }
  printData();
};

document.getElementById("s").addEventListener("click", addData);
