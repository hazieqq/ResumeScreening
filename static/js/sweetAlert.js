function submitNewJobPost() {
    var title = document.getElementById('title').value
    var category = (document.getElementById('category').value == "Choose...") ? "" : document.getElementById('category').value
    console.log(category)
    var jobtype = (document.getElementById('jobtype').value == "Choose...") ? "" : document.getElementById('jobtype').value
    var vacancy = document.getElementById('vacancy').value
    var experience = document.getElementById('experience').value
    var date = document.getElementById('date').value
    var salaryFrom = document.getElementById('salaryFrom').value
    var salaryTo = document.getElementById('SalaryTo').value
    var qualification = document.getElementById('qualification').value
    var description = document.getElementById('description').value
    var status1 = (document.getElementById('status1').checked) ? document.getElementById('status1').value : (document.getElementById('status2').checked) ? document.getElementById('status2').value : ""
    console.log(status1)
    if (title == "" || category == "" || jobtype == "" ||
        vacancy == "" || experience == "" || date == "" || salaryFrom == "" || salaryTo == "" || qualification == "" || description == "" ||
        status1 == "") {
        Swal.fire({
            title: 'Please fill up required information',
            icon: 'warning',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Cancel'
        })
        return
    }
    Swal.fire({
        title: 'Do you want to save the changes?',
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: 'Save',
        denyButtonText: 'Dont save',
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                type: "post",
                url: "/submitNewJobPost",
                data: {
                    'title': title,
                    'category': category,
                    'jobtype': jobtype,
                    'vacancy': vacancy,
                    'experience': experience,
                    'date': date,
                    'salaryFrom': salaryFrom,
                    'salaryTo': salaryTo,
                    'qualification': qualification,
                    'description': description,
                    'status1': status1
                },
                success: function(response) {
                    if (response == "success") {
                        Swal.fire(
                            'Uploaded!',
                            'Your item has been upload.',
                            'success',
                        ).then((result) => {
                            if (result.isConfirmed) {
                                location.reload()
                            } else {
                                location.reload()
                            }
                        })
                    } else {
                        Swal.fire(
                            'Fail!',
                            'Fail to insert into Database. Please try again after 1 minute',
                            'error',
                        ).then((result) => {
                            if (result.isConfirmed) {
                                location.reload()
                            } else {
                                location.reload()
                            }
                        })
                    }
                },
                error: function(errorThrown) {
                    // window.open("../../templates/page-error-500.html")
                    console.log(errorThrown)
                }
            });
        }
    })
}