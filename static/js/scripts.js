'use strict';


const button_1_click = () => {
    document.getElementById("area_0").style.backgroundColor="#FF0000";
};

const testi = () => {
    console.log("JS ajetaan")
}

const show_radio_in_update = () => {
    // Hide all radios
    var radios = document.getElementsByClassName("update_radio")
    for (let i=0; i<radios.length; i++){
        let item = radios[i]
        if (item.hasAttribute("hidden") != true){
            item.setAttribute("hidden", true)
        };
    };
    // Get select value(dinosaur id)
    var select = document.getElementById('select');
    var dinosaur_id = select.options[select.selectedIndex].value;
    console.log("Selected dino id: ")
    console.log(dinosaur_id)
    // Get all elements by name dinosaur_id
    var elements = document.getElementsByName(dinosaur_id);
    for (let i=0; i<elements.length; i++){
        let item = elements[i]
        console.log("Emenent to be shown: ")
        console.log(item)
        if (item.name = dinosaur_id) {
            item.removeAttribute("hidden")
        };
    };
};

