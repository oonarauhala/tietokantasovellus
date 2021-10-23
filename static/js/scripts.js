'use strict';

const map_hover = (area) => {
    console.log("hovering");
    // See notes abt this function
    var map;
    document.querySelectorAll('*').forEach(function(node) {
        if (node.id == "map") {
            console.log(node);
            map = node;
        }
    });
    switch (area) {
        case 1:
            map.src = "static/map_edited_a1.png"
            break;
        case 2:
            map.src = "static/map_edited_a2.png"
            break;
        case 3:
            map.src = "static/map_edited_a3.png"
            break;
        case 4:
            map.src = "static/map_edited_a4.png"
            break;
    };
};

const show_radio_in_update = (class_name, select_id) => {
    // Hide all radios
    var radios = document.getElementsByClassName(class_name)
    for (let i=0; i<radios.length; i++){
        let item = radios[i]
        if (item.hasAttribute("hidden") != true){
            item.setAttribute("hidden", true)
        };
    };
    // Get select value(dinosaur id)
    var select = document.getElementById(select_id);
    var dinosaur_id = select.options[select.selectedIndex].value;
    // Get all elements with name dinosaur_id AND class class_name
    var elements_name = Array.from(document.getElementsByName(dinosaur_id));
    var elements_class = Array.from(document.getElementsByClassName(class_name));
    var elements = elements_name.filter(x => elements_class.includes(x));
    for (let i=0; i<elements.length; i++){
        let item = elements[i]
        if (item.name = dinosaur_id) {
            item.removeAttribute("hidden")
        };
    };
};

