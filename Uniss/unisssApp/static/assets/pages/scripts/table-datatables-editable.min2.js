var TableDatatablesEditable = function() {
    var e = function() {
        function e(e, t) {
            for (var n = e.fnGetData(t), a = $(">td", t), l = 0, r = a.length; r > l; l++) e.fnUpdate(n[l],
                t, l, !1);
            e.fnDraw()
        }

        function t(e, t) {
            var n = e.fnGetData(t),
                a = $(">td", t);
            a[0].innerHTML = '<input type="text" class="form-control input-small" style="height: 25px; margin:0px; padding:2px 5px 2px 5px  ;" value="' + n[0] + '">',
                a[1].innerHTML = '<input type="text" class="form-control input-small"style="height: 25px;margin:0px; padding: 2px 5px 2px 5px ;" value="' + n[1] + '">',
                a[2].innerHTML = '<input type="text" class="form-control input-small"style="height: 25px;margin:0px; padding: 2px 5px 2px 5px ;" value="' + n[2] + '">',
                a[3].innerHTML = '<input type="text" class="form-control input-small"style="height: 25px;margin:0px; padding: 2px 5px 2px 5px ;" value="' + n[3] + '">',
                a[4].innerHTML = '<input type="text" class="form-control input-small"style="height: 25px;margin:0px; padding: 2px 5px 2px 5px ;" value="' + n[4] + '">',
                a[5].innerHTML = '<a class="edit btn blue" style="height: 25px; padding: 2px 5px 2px 5px ;" href="">Guardar</a>',
                a[6].innerHTML = '<a class="cancel btn red" style="height: 25px; padding: 2px 5px 2px 5px ;" href="">Cancelar</a>'
        }

        function n(e, t) {
            var n = $("input", t);
            e.fnUpdate(n[0].value, t, 0, !1),
                e.fnUpdate(n[1].value, t, 1, !1),
                e.fnUpdate(n[2].value, t, 2, !1),
                e.fnUpdate(n[3].value, t, 3, !1),
                e.fnUpdate(n[4].value, t, 4, !1),
                e.fnUpdate('<a class="edit btn blue" style="height: 25px; padding: 2px 5px 2px 5px ;" href="">Editar</a>', t, 5, !1),
                e.fnUpdate('<a class="delete btn red" style="height: 25px; padding: 2px 5px 2px 5px ;" href="">Eliminar</a>', t, 6, !1), e.fnDraw()
        }
        var a = $("#sample_editable_1"),
            l = a.dataTable({
                lengthMenu: [
                    [5, 15, 20, -1],
                    [5, 15, 20, "Todo"]
                ],
                pageLength: 5,
                language: { lengthMenu: " _MENU_ Registros" },
                columnDefs: [{ orderable: !0, targets: [0] }, { searchable: !0, targets: [0] }],
                order: [
                    [0, "asc"]
                ]
            }),
            r = ($("#sample_editable_1_wrapper"), null),
            o = !1;
        $("#sample_editable_1_new").click(function(e) {
                if (e.preventDefault(),
                    o && r) {
                    if (!confirm("Previose row not saved. Do you want to save it ?"))
                        return l.fnDeleteRow(r), r = null, void(o = !1);
                    n(l, r), $(r).find("td:first").html("Untitled"), r = null, o = !1
                }
                var a = l.fnAddData(["", "", "", "", "", ""]),
                    i = l.fnGetNodes(a[0]);
                t(l, i), r = i, o = !0
            }), a.on("click", ".delete", function(e) {
                if (e.preventDefault(), 0 != confirm("Are you sure to delete this row ?")) {
                    var t = $(this).parents("tr")[0];
                    l.fnDeleteRow(t),
                        alert("Deleted! Do not forget to do some ajax to sync with backend :)")
                }
            }),
            a.on("click", ".cancel", function(t) {
                t.preventDefault(), o ? (l.fnDeleteRow(r),
                    r = null, o = !1) : (e(l, r), r = null)
            }), a.on("click", ".edit",
                function(a) {
                    a.preventDefault(), o = !1;
                    var i = $(this).parents("tr")[0];
                    null !== r && r != i ? (e(l, r),
                            t(l, i), r = i) : r == i && "Guardar" == this.innerHTML ? (n(l, r), r = null,
                            alert("Updated! Do not forget to do some ajax to sync with backend :)")) :
                        (t(l, i), r = i)
                })
    };
    return { init: function() { e() } }
}();
jQuery(document).ready(function() { TableDatatablesEditable.init() });