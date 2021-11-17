let addProject = (e) => {
    let pname = document.getElementById("pname").value;
    let desc = document.getElementById("descr").value;
    let ptasks = document.getElementById("ptasks").value;
    if(!(pname.length && desc.length && ptasks.length)){
      e.preventDefault();
      alert("Incomplete Project form!");
    }
  };
  
document.getElementById("p").addEventListener("click", addProject);
