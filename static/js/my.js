function submitNewJobPost() {
    var title = document.getElementById('title').value
    var jobtype = (document.getElementById('jobtype').value == "Choose...") ? "" : document.getElementById('jobtype').value
    var experience = document.getElementById('experience').value
    console.log(experience)
    var date = document.getElementById('date').value
    var salaryFrom = document.getElementById('salaryFrom').value
    salaryFrom = "RM " + salaryFrom;
    var description = tinyMCE.get('description').getContent()
    var status1 = (document.getElementById('status1').checked) ? document.getElementById('status1').value : (document.getElementById('status2').checked) ? document.getElementById('status2').value : ""
    const regex = new RegExp(/^\s*$/);
    if (regex.test(title) || regex.test(jobtype) || experience == "" || date == "" || salaryFrom == "" || regex.test(description) || status1 == "") {
        const swalWithBootstrapButtons = Swal.mixin({
                customClass: {
                    confirmButton: 'btn btn-primary',
                },
                buttonsStyling: false
            })
            // swalWithBootstrapButtons.fire({
            //     title: 'Please fill up required information',
            //     icon: 'warning',
            //     confirmButtonText: 'Cancel'
            // })
        toastr.options = {
            "progressBar": true,
        }
        toastr["warning"]("Please fill up required information");


        return
    }
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger m-2'
        },
        buttonsStyling: false
    })
    swalWithBootstrapButtons.fire({
        title: 'Do you want to save the changes?',
        showCancelButton: true,
        confirmButtonText: 'Save',
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                type: "post",
                url: "/submitNewJobPost",
                data: {
                    'title': title,
                    'jobtype': jobtype,
                    'experience': experience,
                    'date': date,
                    'salaryFrom': salaryFrom,
                    'description': description,
                    'status1': status1
                },
                success: function(response) {
                    if (response == "success") {
                        // Swal.fire(
                        //     'Uploaded!',
                        //     'New job post has been upload.',
                        //     'success',
                        // ).then((result) => {
                        //     if (result.isConfirmed) {
                        //         location.reload()
                        //     } else {
                        //         location.reload()
                        //     }
                        // })
                        toastr["success"]("New job post has been uploaded");
                        $(':input').val('');
                        tinyMCE.get('description').setContent('');
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
            });
        }
    })
}


function deletefunction(id, deletefrom) {
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
                url: "/delete",
                data: {
                    'id': id,
                    'deletefrom': deletefrom
                },
                success: function(response) {
                    if (response == "success") {
                        swalWithBootstrapButtons.fire(
                            'Deleted!',
                            '',
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
                            'Error occured in deleting. Please try again after a few minute',
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
                    Swal.fire(
                        'Fail!',
                        'Error occured in deleting. Please try again after a few minute',
                        'error',
                    ).then((result) => {
                        if (result.isConfirmed) {
                            location.reload()
                        } else {
                            location.reload()
                        }
                    })
                }
            });
        }
    })
}

function updateStatus(elem, id, classnameAnchor) {
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
        url: "/update",
        data: {
            'update': 'updateStatus',
            'jobapplyID': id,
            'text': text
        },
        success: function(response) {
            if (response == "success") {
                // Swal.fire({
                //     // position: 'top-end',
                //     icon: 'success',
                //     heightAuto: false,
                //     title: 'Status has been updated',
                //     showConfirmButton: false,
                //     timer: 1500,
                //     customClass: 'swal-wide',
                // })
                toastr.options = {
                    "progressBar": true,
                }
                toastr["success"]("Successfully updated");
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
    });
}

function editJoblist(id) {

    $("#" + id).find('.edit').hide();
    $("#" + id).find('.edit').siblings().eq(0).show();

    //normal input
    $('#' + id + '').children("td.data ").each(function() {
        var content = $(this).html();
        $(this).html('<input class="form-control solid " value=" ' + content + ' " />');
    });

    // date
    $('#' + id + '').children("td.dataDate").each(function() {
        var content = $(this).html();
        // reverse date since value take only format "y-m-d"
        if (content.match(/^\d{4}-\d{2}-\d{2}$/) === null) {
            //it is not a date with format YYYY-MM-DD
            content = content.split("-").reverse().join("-");
        }
        $(this).html('<input type="date" class="form-control solid form_datetime" value="' + content + '" />');
    });

    // number salary
    $('#' + id + '').children("td.dataNumber").each(function() {
        var content = $(this).html().replace(/^\D+/g, '');
        $(this).html('<input type="number" class="form-control solid number" placeholder="$" min="1000"  value="' + content + '" />');
    });

    // select
    $('#' + id + '').children("td.dataSelectType").each(function() {
        var content = $(this).html();
        if (content.includes("Full")) {
            $(this).html('<select class="select"><option selected>Full Employee</option><option>Internship/Graduate Trainee</option></select>');
        } else {
            $(this).html('<select class="select"><option>Permanent Employee</option><option selected>Internship/Graduate Trainee</option></select>');
        }
    });

    // select status
    $('#' + id + '').children("td.dataSelectStatus").each(function() {
        var content = $(this).children().html();
        if (content.toLowerCase() == "active") {
            $(this).html('<select class="dataSelectStatus"><option selected><span class="badge badge-success badge-lg light ">Active</span></option><option><span class="badge badge-danger badge-lg light ">Inactive</span></option></select>');
        } else {
            $(this).html('<select class="dataSelectStatus"><option ><span class="badge badge-success badge-lg light ">Active</span></option><option selected><span class="badge badge-danger badge-lg light ">Inactive</span></option></select>');
        }
    });

    // select experience
    $('#' + id + '').children("td.dataSelectExp").each(function() {
        var content = $(this).html();
        if (content.includes("1")) {
            $(this).html('<select class="dataSelectExp"><option>None</option><option selected>1 Yr</option><option>3 Yr</option><option>more than 5 years</option></select>');
        } else if (content.includes("3")) {
            $(this).html('<select class="dataSelectExp"><option>None</option><option >1 Yr</option><option selected>3 Yr</option><option>more than 5 years</option></select>');
        } else if (content.includes("None")) {
            $(this).html('<select class="dataSelectExp"><option selected>None</option><option >1 Yr</option><option >3 Yr</option><option>more than 5 years</option></select>');
        } else {
            $(this).html('<select class="dataSelectExp"><option>None</option><option >1 Yr</option><option >3 Yr</option><option selected>more than 5 years</option></select>');
        }
    });


    //textArea
    $('#' + id + '').children("td.dataTextArea ").each(function() {
        $(this).html('<a style="color:#FF4500; " data-bs-toggle="modal" data-bs-target="#exampleModalCenter1' + id + '">Click to edit</a>');
    });

    $('#' + id + '').on('click', '.save', function() {
        var checkEmpty = 0;
        $('#' + id + '').find("input ").map(function() {
            $(this).each(function() {
                // check white space and empty string
                const regex = new RegExp(/^\s*$/);
                var content;
                if (regex.test($(this).val())) {
                    content = "NA";
                    checkEmpty = 1;
                } else {
                    content = $(this).val();
                }
                if (this.classList.contains("number")) {
                    $(this).html("RM " + content);
                } else {
                    $(this).html(content);
                }
                if (checkEmpty == 0) {
                    $(this).contents().unwrap()
                }

            });
        }).get();
        if (checkEmpty == 0) {
            $('#' + id + '').find("select").map(function() {
                $(this).each(function() {
                    var content = $(this).val();
                    // make sure dataselect1 class is not remove
                    if (this.classList.contains("dataSelectStatus")) {
                        if (content == "Active") {
                            $('#' + id + '').children("td.dataSelectStatus ").each(function() {
                                $(this).html('<span class="badge badge-success badge-lg light">Active</span>');
                            });
                        } else {
                            $('#' + id + '').children("td.dataSelectStatus ").each(function() {
                                $(this).html('<span class="badge badge-danger badge-lg light">Inactive</span>');
                            });
                        }
                    } else {
                        $(this).html(content);
                    }
                    if (checkEmpty == 0) {
                        $(this).contents().unwrap()
                    }
                });
            }).get();

            $('#' + id + '').children("td.dataTextArea ").each(function() {
                $(this).html('<a style="color:#FF4500; " data-bs-toggle="modal" data-bs-target="#exampleModalCenter2' + id + '">Click to view</a>');
                //console.log($("#exampleModalCenter2" + id).find('textarea').val());
            });
        }



        //$(this).siblings('.edit').show();
        //$(this).hide();
        updateJobList(id, checkEmpty);
    });

}

tinymce.init({
    selector: 'textarea.mceNoEditor',
    readonly: true
});

tinymce.init({
    selector: 'textarea',
});

// $('.select').select2({
//     theme: 'bootstrap4',
// });

function modalSave(id, el) {

    const message = document.getElementById('description' + id);
    message.innerHTML = tinyMCE.get('description' + id).getContent();
    $("#exampleModalCenter2" + id).find('textarea').html(tinyMCE.get('description' + id).getContent());
    tinyMCE.get('description2' + id).setContent(tinyMCE.get('description' + id).getContent());

}

function updateJobList(id, checkEmpty) {
    var title = $("#" + id).find('#title').html();
    var type = $("#" + id).find('#type').html();
    var salary = $("#" + id).find('#salary').html();
    var postedDate = $("#" + id).find('#postedDate').html();
    var closedDate = $("#" + id).find('#closedDate').html();
    var status = $("#" + id).find('#status').html();
    var re = status,
        m = /(?<=<span.*?>)(.*?)(?=<\/span>)/g,
        s = re.match(m);
    status = JSON.stringify(s).replace(/[^a-zA-Z0-9,;\-.!? ]/g, '');
    var description = tinyMCE.get('description2' + id).getContent();
    var exp = $("#" + id).find('#exp').html();
    if (checkEmpty != 0) {
        toastr.options = {
            "progressBar": true,
        }
        toastr["warning"]("Please fill up required information");
        //editJoblist(id);
    } else {
        $("#" + id).find('.save').siblings('.edit').show();
        $("#" + id).find('.save').hide();
        $.ajax({
            type: "post",
            url: "/update",
            data: {
                'update': 'updateJobList',
                'id': id,
                'title': title,
                'type': type,
                'salary': salary,
                'postedDate': postedDate,
                'closedDate': closedDate,
                'status': status,
                'description': description,
                'exp': exp
            },
            success: function(response) {
                if (response == "success") {
                    // Swal.fire({
                    //     // position: 'top-end',
                    //     icon: 'success',
                    //     heightAuto: false,
                    //     title: 'Status has been updated',
                    //     showConfirmButton: false,
                    //     timer: 1500,
                    //     customClass: 'swal-wide',
                    // })
                    toastr.options = {
                        "progressBar": true,
                    }
                    toastr["success"]("Successfully updated");
                } else {
                    Swal.fire(
                        'Fail!',
                        'Error occur in updating job list. Please try again after a few minute',
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
                Swal.fire(
                    'Fail!',
                    'Error occur in updating job list. Please try again after a few minute',
                    'error',
                ).then((result) => {
                    if (result.isConfirmed) {
                        location.reload()
                    } else {
                        location.reload()
                    }
                })
            }
        });
    }



}