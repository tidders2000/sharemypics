{"filter":false,"title":"javascript.js","tooltip":"/static/js/javascript.js","undoManager":{"mark":74,"position":74,"stack":[[{"start":{"row":16,"column":0},"end":{"row":54,"column":3},"action":"insert","lines":["$(function() {","  // Initialize form validation on the registration form.","  // It has the name attribute \"registration\"","  $(\"form[name='registration']\").validate({","    // Specify validation rules","    rules: {","      // The key name on the left side is the name attribute","      // of an input field. Validation rules are defined","      // on the right side","      firstname: \"required\",","      lastname: \"required\",","      email: {","        required: true,","        // Specify that email should be validated","        // by the built-in \"email\" rule","        email: true","      },","      password: {","        required: true,","        minlength: 5","      }","    },","    // Specify validation error messages","    messages: {","      firstname: \"Please enter your firstname\",","      lastname: \"Please enter your lastname\",","      password: {","        required: \"Please provide a password\",","        minlength: \"Your password must be at least 5 characters long\"","      },","      email: \"Please enter a valid email address\"","    },","    // Make sure the form is submitted to the destination defined","    // in the \"action\" attribute of the form when valid","    submitHandler: function(form) {","      form.submit();","    }","  });","});"],"id":71}],[{"start":{"row":17,"column":2},"end":{"row":18,"column":45},"action":"remove","lines":["// Initialize form validation on the registration form.","  // It has the name attribute \"registration\""],"id":72}],[{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"insert","lines":["/"],"id":73},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"insert","lines":["/"]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["i"]}],[{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["n"],"id":74},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["i"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["t"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["i"]},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["a"]},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["l"]},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["i"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["s"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":[" "],"id":75},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["f"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["o"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["r"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["m"]}],[{"start":{"row":17,"column":19},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":76},{"start":{"row":18,"column":0},"end":{"row":18,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":19,"column":16},"end":{"row":19,"column":28},"action":"remove","lines":["registration"],"id":77},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["q"]},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":["u"]},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["a"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["n"]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["i"],"id":78},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":16},"end":{"row":19,"column":23},"action":"remove","lines":["quantit"],"id":79},{"start":{"row":19,"column":16},"end":{"row":19,"column":29},"action":"insert","lines":["quantity_form"]}],[{"start":{"row":22,"column":6},"end":{"row":24,"column":26},"action":"remove","lines":["// The key name on the left side is the name attribute","      // of an input field. Validation rules are defined","      // on the right side"],"id":80}],[{"start":{"row":20,"column":7},"end":{"row":20,"column":14},"action":"remove","lines":["Specify"],"id":81}],[{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"remove","lines":["s"],"id":82}],[{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":[" "],"id":83},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["t"]},{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":["o"]}],[{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":[" "],"id":84},{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["s"]},{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"insert","lines":["t"]},{"start":{"row":17,"column":25},"end":{"row":17,"column":26},"action":"insert","lines":["o"]},{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"insert","lines":["p"]}],[{"start":{"row":17,"column":27},"end":{"row":17,"column":28},"action":"insert","lines":[" "],"id":85},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["0"]}],[{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":[" "],"id":86},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["q"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["u"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"insert","lines":["a"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["n"]},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":["i"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["t"]},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"insert","lines":["y"]}],[{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"insert","lines":[" "],"id":87},{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"insert","lines":["b"]},{"start":{"row":17,"column":39},"end":{"row":17,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":39},"end":{"row":17,"column":40},"action":"remove","lines":["e"],"id":88},{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"remove","lines":["b"]},{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"remove","lines":[" "]},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"remove","lines":["y"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"remove","lines":["t"]},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"remove","lines":["i"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"remove","lines":["n"]}],[{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["n"],"id":89},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":["t"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["i"]},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"insert","lines":["t"]},{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"insert","lines":["y"]}],[{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"insert","lines":[" "],"id":90},{"start":{"row":17,"column":39},"end":{"row":17,"column":40},"action":"insert","lines":["b"]},{"start":{"row":17,"column":40},"end":{"row":17,"column":41},"action":"insert","lines":["e"]},{"start":{"row":17,"column":41},"end":{"row":17,"column":42},"action":"insert","lines":["i"]},{"start":{"row":17,"column":42},"end":{"row":17,"column":43},"action":"insert","lines":["n"]},{"start":{"row":17,"column":43},"end":{"row":17,"column":44},"action":"insert","lines":["g"]}],[{"start":{"row":17,"column":44},"end":{"row":17,"column":45},"action":"insert","lines":[" "],"id":91},{"start":{"row":17,"column":45},"end":{"row":17,"column":46},"action":"insert","lines":["e"]},{"start":{"row":17,"column":46},"end":{"row":17,"column":47},"action":"insert","lines":["n"]},{"start":{"row":17,"column":47},"end":{"row":17,"column":48},"action":"insert","lines":["t"]},{"start":{"row":17,"column":48},"end":{"row":17,"column":49},"action":"insert","lines":["e"]},{"start":{"row":17,"column":49},"end":{"row":17,"column":50},"action":"insert","lines":["r"]},{"start":{"row":17,"column":50},"end":{"row":17,"column":51},"action":"insert","lines":["e"]},{"start":{"row":17,"column":51},"end":{"row":17,"column":52},"action":"insert","lines":["d"]}],[{"start":{"row":17,"column":52},"end":{"row":17,"column":53},"action":"insert","lines":[" "],"id":92},{"start":{"row":17,"column":53},"end":{"row":17,"column":54},"action":"insert","lines":["b"]},{"start":{"row":17,"column":54},"end":{"row":17,"column":55},"action":"insert","lines":["y"]}],[{"start":{"row":17,"column":55},"end":{"row":17,"column":56},"action":"insert","lines":[" "],"id":93},{"start":{"row":17,"column":56},"end":{"row":17,"column":57},"action":"insert","lines":["u"]},{"start":{"row":17,"column":57},"end":{"row":17,"column":58},"action":"insert","lines":["s"]},{"start":{"row":17,"column":58},"end":{"row":17,"column":59},"action":"insert","lines":["e"]},{"start":{"row":17,"column":59},"end":{"row":17,"column":60},"action":"insert","lines":["r"]}],[{"start":{"row":16,"column":14},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":94},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["\t"]}],[{"start":{"row":24,"column":6},"end":{"row":24,"column":15},"action":"remove","lines":["firstname"],"id":95},{"start":{"row":24,"column":6},"end":{"row":24,"column":7},"action":"insert","lines":["q"]},{"start":{"row":24,"column":7},"end":{"row":24,"column":8},"action":"insert","lines":["u"]},{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"insert","lines":["a"]},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["t"],"id":96},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["i"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["y"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["u"]}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"remove","lines":["u"],"id":97},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"remove","lines":["y"]},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"remove","lines":["i"]}],[{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["i"],"id":98},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["t"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["y"]}],[{"start":{"row":32,"column":4},"end":{"row":35,"column":7},"action":"remove","lines":["  password: {","        required: true,","        minlength: 5","      }"],"id":99}],[{"start":{"row":26,"column":5},"end":{"row":31,"column":8},"action":"remove","lines":[" email: {","        required: true,","        // Specify that email should be validated","        // by the built-in \"email\" rule","        email: true","      },"],"id":100}],[{"start":{"row":25,"column":5},"end":{"row":25,"column":27},"action":"remove","lines":[" lastname: \"required\","],"id":101}],[{"start":{"row":31,"column":6},"end":{"row":31,"column":15},"action":"remove","lines":["firstname"],"id":102},{"start":{"row":31,"column":6},"end":{"row":31,"column":7},"action":"insert","lines":["q"]},{"start":{"row":31,"column":7},"end":{"row":31,"column":8},"action":"insert","lines":["u"]},{"start":{"row":31,"column":8},"end":{"row":31,"column":9},"action":"insert","lines":["a"]},{"start":{"row":31,"column":9},"end":{"row":31,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":31,"column":10},"end":{"row":31,"column":11},"action":"insert","lines":["t"],"id":103},{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"insert","lines":["i"]},{"start":{"row":31,"column":12},"end":{"row":31,"column":13},"action":"insert","lines":["t"]},{"start":{"row":31,"column":13},"end":{"row":31,"column":14},"action":"insert","lines":["y"]}],[{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"insert","lines":[" "],"id":104},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"insert","lines":["m"]},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"insert","lines":["u"]},{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"remove","lines":["s"],"id":105},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"remove","lines":["u"]},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"remove","lines":["m"]},{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"remove","lines":[" "]}],[{"start":{"row":31,"column":17},"end":{"row":31,"column":44},"action":"remove","lines":["Please enter your firstname"],"id":106},{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"insert","lines":["M"]},{"start":{"row":31,"column":18},"end":{"row":31,"column":19},"action":"insert","lines":["u"]},{"start":{"row":31,"column":19},"end":{"row":31,"column":20},"action":"insert","lines":["s"]},{"start":{"row":31,"column":20},"end":{"row":31,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":31,"column":21},"end":{"row":31,"column":22},"action":"insert","lines":[" "],"id":107},{"start":{"row":31,"column":22},"end":{"row":31,"column":23},"action":"insert","lines":["b"]},{"start":{"row":31,"column":23},"end":{"row":31,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":31,"column":24},"end":{"row":31,"column":25},"action":"insert","lines":[" "],"id":108},{"start":{"row":31,"column":25},"end":{"row":31,"column":26},"action":"insert","lines":["g"]},{"start":{"row":31,"column":26},"end":{"row":31,"column":27},"action":"insert","lines":["r"]},{"start":{"row":31,"column":27},"end":{"row":31,"column":28},"action":"insert","lines":["e"]},{"start":{"row":31,"column":28},"end":{"row":31,"column":29},"action":"insert","lines":["a"]},{"start":{"row":31,"column":29},"end":{"row":31,"column":30},"action":"insert","lines":["t"]},{"start":{"row":31,"column":30},"end":{"row":31,"column":31},"action":"insert","lines":["e"]},{"start":{"row":31,"column":31},"end":{"row":31,"column":32},"action":"insert","lines":["r"]}],[{"start":{"row":31,"column":32},"end":{"row":31,"column":33},"action":"insert","lines":[" "],"id":109},{"start":{"row":31,"column":33},"end":{"row":31,"column":34},"action":"insert","lines":["t"]},{"start":{"row":31,"column":34},"end":{"row":31,"column":35},"action":"insert","lines":["h"]},{"start":{"row":31,"column":35},"end":{"row":31,"column":36},"action":"insert","lines":["a"]},{"start":{"row":31,"column":36},"end":{"row":31,"column":37},"action":"insert","lines":["n"]}],[{"start":{"row":31,"column":37},"end":{"row":31,"column":38},"action":"insert","lines":[" "],"id":110},{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"insert","lines":["0"]}],[{"start":{"row":32,"column":6},"end":{"row":37,"column":49},"action":"remove","lines":["lastname: \"Please enter your lastname\",","      password: {","        required: \"Please provide a password\",","        minlength: \"Your password must be at least 5 characters long\"","      },","      email: \"Please enter a valid email address\""],"id":111}],[{"start":{"row":29,"column":7},"end":{"row":29,"column":26},"action":"remove","lines":["Specify validation "],"id":112}],[{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"remove","lines":["s"],"id":113}],[{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"remove","lines":["d"],"id":116},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"remove","lines":["e"]},{"start":{"row":24,"column":22},"end":{"row":24,"column":23},"action":"remove","lines":["r"]},{"start":{"row":24,"column":21},"end":{"row":24,"column":22},"action":"remove","lines":["i"]},{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"remove","lines":["u"]},{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"remove","lines":["q"]},{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"remove","lines":["e"]},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"remove","lines":["r"]}],[{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["m"],"id":117},{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"insert","lines":["i"]},{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"insert","lines":["n"]},{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"insert","lines":["-"]},{"start":{"row":24,"column":21},"end":{"row":24,"column":22},"action":"insert","lines":["1"]}],[{"start":{"row":24,"column":16},"end":{"row":24,"column":23},"action":"remove","lines":["\"min-1\""],"id":118},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"remove","lines":[" "]}],[{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["{"],"id":119},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["}"]}],[{"start":{"row":24,"column":16},"end":{"row":26,"column":6},"action":"insert","lines":["","      \t","      "],"id":120}],[{"start":{"row":25,"column":7},"end":{"row":26,"column":13},"action":"insert","lines":["required: true,","      min: 13"],"id":121}],[{"start":{"row":26,"column":6},"end":{"row":26,"column":7},"action":"insert","lines":[" "],"id":122},{"start":{"row":26,"column":7},"end":{"row":26,"column":8},"action":"insert","lines":[" "]}],[{"start":{"row":26,"column":14},"end":{"row":26,"column":15},"action":"remove","lines":["3"],"id":123}],[{"start":{"row":20,"column":5},"end":{"row":20,"column":31},"action":"remove","lines":["form[name='quantity_form']"],"id":124}],[{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"insert","lines":["£"],"id":125},{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"remove","lines":["f"],"id":126},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"remove","lines":["£"]}],[{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"insert","lines":["#"],"id":127}],[{"start":{"row":20,"column":6},"end":{"row":20,"column":19},"action":"insert","lines":["quantity_form"],"id":128}],[{"start":{"row":36,"column":6},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":138},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]},{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"insert","lines":["e"]},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"insert","lines":["r"]},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"insert","lines":["r"]},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":["o"]},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":["r"]},{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"insert","lines":["E"]}],[{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"insert","lines":["l"],"id":139},{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"insert","lines":["e"]},{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"insert","lines":["m"]},{"start":{"row":37,"column":13},"end":{"row":37,"column":14},"action":"insert","lines":["e"]},{"start":{"row":37,"column":14},"end":{"row":37,"column":15},"action":"insert","lines":["n"]},{"start":{"row":37,"column":15},"end":{"row":37,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":37,"column":16},"end":{"row":37,"column":17},"action":"insert","lines":[":"],"id":140}],[{"start":{"row":37,"column":17},"end":{"row":37,"column":18},"action":"insert","lines":[" "],"id":141}],[{"start":{"row":37,"column":18},"end":{"row":37,"column":20},"action":"insert","lines":["''"],"id":142}],[{"start":{"row":37,"column":19},"end":{"row":37,"column":20},"action":"insert","lines":["d"],"id":143},{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"insert","lines":["i"]},{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"insert","lines":["v"]}],[{"start":{"row":37,"column":23},"end":{"row":37,"column":24},"action":"insert","lines":[","],"id":144}],[{"start":{"row":37,"column":24},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":145},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":5},"action":"insert","lines":["e"],"id":146},{"start":{"row":38,"column":5},"end":{"row":38,"column":6},"action":"insert","lines":["r"]},{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"insert","lines":["r"]},{"start":{"row":38,"column":7},"end":{"row":38,"column":8},"action":"insert","lines":["o"]},{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"insert","lines":["r"]}],[{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"insert","lines":["L"],"id":147},{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"insert","lines":["a"]},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"insert","lines":["b"]},{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"insert","lines":["e"]},{"start":{"row":38,"column":13},"end":{"row":38,"column":14},"action":"insert","lines":["l"]},{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"insert","lines":["C"]},{"start":{"row":38,"column":15},"end":{"row":38,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":38,"column":16},"end":{"row":38,"column":17},"action":"insert","lines":["n"],"id":148},{"start":{"row":38,"column":17},"end":{"row":38,"column":18},"action":"insert","lines":["t"]},{"start":{"row":38,"column":18},"end":{"row":38,"column":19},"action":"insert","lines":["a"]},{"start":{"row":38,"column":19},"end":{"row":38,"column":20},"action":"insert","lines":["i"]},{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"insert","lines":["n"]},{"start":{"row":38,"column":21},"end":{"row":38,"column":22},"action":"insert","lines":["e"]},{"start":{"row":38,"column":22},"end":{"row":38,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":38,"column":23},"end":{"row":38,"column":24},"action":"insert","lines":[":"],"id":149}],[{"start":{"row":38,"column":24},"end":{"row":38,"column":25},"action":"insert","lines":[" "],"id":150}],[{"start":{"row":38,"column":25},"end":{"row":38,"column":27},"action":"insert","lines":["''"],"id":151}],[{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"insert","lines":["e"],"id":152},{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"insert","lines":["r"]},{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"insert","lines":["r"]},{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"insert","lines":["o"]}],[{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"remove","lines":["o"],"id":153},{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"remove","lines":["r"]},{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"remove","lines":["r"]},{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"remove","lines":["e"]}],[{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"insert","lines":["."],"id":154},{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"insert","lines":["e"]},{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"insert","lines":["r"]},{"start":{"row":38,"column":29},"end":{"row":38,"column":30},"action":"insert","lines":["r"]},{"start":{"row":38,"column":30},"end":{"row":38,"column":31},"action":"insert","lines":["o"]},{"start":{"row":38,"column":31},"end":{"row":38,"column":32},"action":"insert","lines":["r"]}],[{"start":{"row":38,"column":32},"end":{"row":38,"column":33},"action":"insert","lines":["t"],"id":155},{"start":{"row":38,"column":33},"end":{"row":38,"column":34},"action":"insert","lines":["x"]},{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":38,"column":36},"end":{"row":38,"column":37},"action":"insert","lines":[","],"id":156}]]},"ace":{"folds":[],"scrolltop":357,"scrollleft":0,"selection":{"start":{"row":42,"column":20},"end":{"row":42,"column":20},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":12,"state":"start","mode":"ace/mode/javascript"}},"timestamp":1565214398931,"hash":"2308fb3aef1c3abbe4d8f0672bc7ef2ebcb9c5a6"}