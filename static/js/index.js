function deleteEmployee(id){
    axios.delete(`/employee/delete/${id}`)
    .then(res => {
        swal("Employee Deleted", res.data, "success")
        .then(value => location.reload())
    })
    .catch(err => swal("Employee Cannot be Deleted", "Error : " + err.message, "error"))
}

document.getElementById('editForm').addEventListener('submit', function(e){
    e.preventDefault();
    const options = {
        headers : {
            'Content-Type' : 'Application/json'
        }
    }
    let elements = document.getElementById("editForm").elements;
    const formData = new FormData();
    for(let i = 0 ; i < elements.length ; i++){
        let item = elements.item(i);
        formData.append(item.name, item.value)
    }
    const id = document.getElementById('employee_id').value;
    axios.put(`/employee/update/${id}`, formData, options)
    .then(res =>{
        swal("Employee Updated", res.data, "success")
        .then(value => location.assign('/'))
    })
    .catch(err => swal(err.message, '', 'error'))
})