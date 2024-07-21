$(document).ready(function() {
    loadData();

    $("#addEditForm").submit(function(event) {
        event.preventDefault();
        saveData();
    });
});

function loadData() {
    $.getJSON("/api/clients", function(data) {
        var clientsTableBody = $("#clients-table-body");
        clientsTableBody.empty();
        $.each(data, function(index, item) {
            clientsTableBody.append(
                "<tr>" +
                "<td>" + item.id + "</td>" +
                "<td>" + item.fio + "</td>" +
                "<td>" + item.region + "</td>" +
                "<td>" + item.size + "</td>" +
                "<td>" + item.email + "</td>" +
                "<td>" + item.phone + "</td>" +
                "<td><button class='btn btn-danger' onclick='deleteRecord(\"clients\", " + item.id + ")'>Удалить</button> " +
                "<button class='btn btn-primary' onclick='openEditModal(\"clients\", " + item.id + ")'>Редактировать</button></td>" +
                "</tr>"
            );
        });
    });

    $.getJSON("/api/staff", function(data) {
        var staffTableBody = $("#staff-table-body");
        staffTableBody.empty();
        $.each(data, function(index, item) {
            staffTableBody.append(
                "<tr>" +
                "<td>" + item.id + "</td>" +
                "<td>" + item.first_name + "</td>" +
                "<td>" + item.last_name + "</td>" +
                "<td>" + item.patronymic + "</td>" +
                "<td>" + item.photo + "</td>" +
                "<td>" + item.description + "</td>" +
                "<td>" + item.phrase + "</td>" +
                "<td><button class='btn btn-danger' onclick='deleteRecord(\"staff\", " + item.id + ")'>Удалить</button> " +
                "<button class='btn btn-primary' onclick='openEditModal(\"staff\", " + item.id + ")'>Редактировать</button></td>" +
                "</tr>"
            );
        });
    });

    $.getJSON("/api/portfolio", function(data) {
        var portfolioTableBody = $("#portfolio-table-body");
        portfolioTableBody.empty();
        $.each(data, function(index, item) {
            portfolioTableBody.append(
                "<tr>" +
                "<td>" + item.id + "</td>" +
                "<td>" + item.storage_name + "</td>" +
                "<td>" + item.size + "</td>" +
                "<td>" + item.location + "</td>" +
                "<td>" + item.description + "</td>" +
                "<td>" + item.images + "</td>" +
                "<td><button class='btn btn-danger' onclick='deleteRecord(\"portfolio\", " + item.id + ")'>Удалить</button> " +
                "<button class='btn btn-primary' onclick='openEditModal(\"portfolio\", " + item.id + ")'>Редактировать</button></td>" +
                "</tr>"
            );
        });
    });
}

function openAddModal(type) {
    $("#addEditModalLabel").text("Добавить запись");
    $("#addEditForm").data("type", type);
    $("#addEditForm").data("id", null);
    fillFormFields(type);
    $("#addEditModal").modal("show");
}

function openEditModal(type, id) {
    $("#addEditModalLabel").text("Редактировать запись");
    $("#addEditForm").data("type", type);
    $("#addEditForm").data("id", id);
    fillFormFields(type, id);
    $("#addEditModal").modal("show");
}

function fillFormFields(type, id = null) {
    var formFields = $("#addEditForm");
    formFields.empty();

    if (type == "clients") {
        formFields.append(
            '<div class="mb-3">' +
            '<label for="fio" class="form-label">ФИО</label>' +
            '<input type="text" class="form-control" id="fio" name="fio" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="region" class="form-label">Регион</label>' +
            '<input type="text" class="form-control" id="region" name="region" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="size" class="form-label">Квадратура</label>' +
            '<input type="text" class="form-control" id="size" name="size" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="email" class="form-label">E-mail</label>' +
            '<input type="email" class="form-control" id="email" name="email" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="phone" class="form-label">Телефон</label>' +
            '<input type="tel" class="form-control" id="phone" name="phone" required>' +
            '</div>'
        );
    } else if (type == "staff") {
        formFields.append(
            '<div class="mb-3">' +
            '<label for="first_name" class="form-label">Имя</label>' +
            '<input type="text" class="form-control" id="first_name" name="first_name" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="last_name" class="form-label">Фамилия</label>' +
            '<input type="text" class="form-control" id="last_name" name="last_name" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="patronymic" class="form-label">Отчество</label>' +
            '<input type="text" class="form-control" id="patronymic" name="patronymic" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="photo" class="form-label">Фото</label>' +
            '<input type="text" class="form-control" id="photo" name="photo" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="description" class="form-label">Описание</label>' +
            '<input type="text" class="form-control" id="description" name="description" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="phrase" class="form-label">Фраза</label>' +
            '<input type="text" class="form-control" id="phrase" name="phrase" required>' +
            '</div>'
        );
    } else if (type == "portfolio") {
        formFields.append(
            '<div class="mb-3">' +
            '<label for="storage_name" class="form-label">Имя хранения</label>' +
            '<input type="text" class="form-control" id="storage_name" name="storage_name" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="size" class="form-label">Квадратура</label>' +
            '<input type="text" class="form-control" id="size" name="size" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="location" class="form-label">Расположение</label>' +
            '<input type="text" class="form-control" id="location" name="location" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="description" class="form-label">Описание</label>' +
            '<input type="text" class="form-control" id="description" name="description" required>' +
            '</div>' +
            '<div class="mb-3">' +
            '<label for="images" class="form-label">Картинки</label>' +
            '<input type="text" class="form-control" id="images" name="images" required>' +
            '</div>'
        );
    }

    if (id) {
        // If editing, fetch and populate the existing data
        $.getJSON("/api/" + type + "/" + id, function(data) {
            $.each(data, function(key, value) {
                $("#addEditForm [name='" + key + "']").val(value);
            });
        });
    }
}

function saveData() {
    var type = $("#addEditForm").data("type");
    var id = $("#addEditForm").data("id");
    var url = "/api/" + type;
    var method = "POST";

    if (id) {
        url += "/" + id;
        method = "PUT";
    }

    $.ajax({
        url: url,
        method: method,
        data: $("#addEditForm").serialize(),
        success: function() {
            $("#addEditModal").modal("hide");
            loadData();
        }
    });
}

function deleteRecord(type, id) {
    if (confirm("Вы уверены, что хотите удалить эту запись?")) {
        $.ajax({
            url: "/api/" + type + "/" + id,
            method: "DELETE",
            success: function() {
                loadData();
            }
        });
    }
}
