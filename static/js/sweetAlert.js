function submitNewJobPost() {
    var title = document.getElementById('title').value
    var category = (document.getElementById('category').value == "Choose...") ? "" : document.getElementById('category').value
    var jobtype = (document.getElementById('jobtype').value == "Choose...") ? "" : document.getElementById('jobtype').value
    var vacancy = document.getElementById('vacancy').value
    var experience = document.getElementById('experience').value
    var date = document.getElementById('date').value
    var salaryFrom = document.getElementById('salaryFrom').value
    var salaryTo = document.getElementById('SalaryTo').value
    var qualification = document.getElementById('qualification').value
    var description = tinyMCE.get('description').getContent()
    console.log(description)
    var status1 = (document.getElementById('status1').checked) ? document.getElementById('status1').value : (document.getElementById('status2').checked) ? document.getElementById('status2').value : ""
    if (title == "" || category == "" || jobtype == "" ||
        vacancy == "" || experience == "" || date == "" || salaryFrom == "" || salaryTo == "" || qualification == "" || description == "" ||
        status1 == "") {
        const swalWithBootstrapButtons = Swal.mixin({
            customClass: {
                confirmButton: 'btn btn-primary',
            },
            buttonsStyling: false
        })
        swalWithBootstrapButtons.fire({
            title: 'Please fill up required information',
            icon: 'warning',
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
                            'New job post has been upload.',
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


function deleteJobApply(jobapplyID) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            actions: "my-actions",
            confirmButton: 'btn btn-danger',
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        confirmButtonText: 'Yes, delete it!',
        showCloseButton: true
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                type: "post",
                url: "/deleteJobApply",
                data: {
                    'jobapplyID': jobapplyID
                },
                success: function(response) {
                    if (response == "success") {
                        swalWithBootstrapButtons.fire(
                            'Deleted!',
                            'Your file has been deleted.',
                            'success'
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
                            'Error occur in deleting the application. Please try again after a few minute',
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

function checkID(elem, id, classnameAnchor) {
    var text = elem.text;
    const btn = document.getElementById(id);
    btn.classList.remove('btn-warning', 'btn-danger', 'btn-success');
    // change button color
    btn.classList.add(classnameAnchor);
    // change text
    btn.innerHTML = text;

    // update database using ajax to call flask
    $.ajax({
        type: "post",
        url: "/updateStatusApplication",
        data: {
            'jobapplyID': id,
            'text': text
        },
        success: function(response) {
            if (response == "success") {
                Swal.fire({
                    // position: 'top-end',
                    icon: 'success',
                    heightAuto: false,
                    title: 'Status has been updated',
                    showConfirmButton: false,
                    timer: 1500,
                    customClass: 'swal-wide',
                })
            } else {
                Swal.fire(
                    'Fail!',
                    'Error occur in updating the status. Please try again after a few minute',
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