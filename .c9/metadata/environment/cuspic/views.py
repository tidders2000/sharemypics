{"filter":false,"title":"views.py","tooltip":"/cuspic/views.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":29,"column":45},"end":{"row":29,"column":46},"action":"insert","lines":["."],"id":255},{"start":{"row":29,"column":46},"end":{"row":29,"column":47},"action":"insert","lines":["i"]},{"start":{"row":29,"column":47},"end":{"row":29,"column":48},"action":"insert","lines":["m"]},{"start":{"row":29,"column":48},"end":{"row":29,"column":49},"action":"insert","lines":["a"]},{"start":{"row":29,"column":49},"end":{"row":29,"column":50},"action":"insert","lines":["g"]},{"start":{"row":29,"column":50},"end":{"row":29,"column":51},"action":"insert","lines":["e"]}],[{"start":{"row":29,"column":34},"end":{"row":29,"column":52},"action":"remove","lines":[".format(img.image)"],"id":256}],[{"start":{"row":29,"column":31},"end":{"row":29,"column":33},"action":"remove","lines":["{}"],"id":257},{"start":{"row":29,"column":30},"end":{"row":29,"column":31},"action":"remove","lines":["/"]}],[{"start":{"row":29,"column":30},"end":{"row":29,"column":31},"action":"insert","lines":["/"],"id":258}],[{"start":{"row":29,"column":30},"end":{"row":29,"column":31},"action":"remove","lines":["/"],"id":259}],[{"start":{"row":29,"column":30},"end":{"row":29,"column":31},"action":"insert","lines":["/"],"id":260}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":34},"action":"insert","lines":["s3_resource = boto3.resource('s3')"],"id":261}],[{"start":{"row":29,"column":7},"end":{"row":33,"column":85},"action":"remove","lines":[" cloudFilename = 'media/'","        session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)","        s3 = session.resource('s3')","        s3.Bucket(AWS_STORAGE_BUCKET_NAME).upload_file(photo, cloudFilename)","        #s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(Key=cloudFilename, Body=photo)"],"id":262}],[{"start":{"row":29,"column":7},"end":{"row":30,"column":29},"action":"insert","lines":["s3_resource.Object(first_bucket_name, first_file_name).upload_file(","    Filename=first_file_name)"],"id":263}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"insert","lines":[" "],"id":264},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"insert","lines":[" "]},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"insert","lines":[" "]},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"insert","lines":[" "]}],[{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"remove","lines":["F"],"id":265}],[{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"insert","lines":["F"],"id":266}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":8},"action":"remove","lines":["    "],"id":267}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"insert","lines":[" "],"id":268},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"insert","lines":[" "]},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"insert","lines":[" "]}],[{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"remove","lines":[" "],"id":269},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"remove","lines":[" "]},{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":[" "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["    "]},{"start":{"row":29,"column":74},"end":{"row":30,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":29,"column":26},"end":{"row":29,"column":43},"action":"remove","lines":["first_bucket_name"],"id":270},{"start":{"row":29,"column":26},"end":{"row":29,"column":48},"action":"insert","lines":["AWS_STORAGE_BUCKET_NAM"]}],[{"start":{"row":29,"column":48},"end":{"row":29,"column":49},"action":"insert","lines":["E"],"id":271}],[{"start":{"row":29,"column":65},"end":{"row":29,"column":66},"action":"remove","lines":["e"],"id":272},{"start":{"row":29,"column":64},"end":{"row":29,"column":65},"action":"remove","lines":["m"]}],[{"start":{"row":29,"column":88},"end":{"row":29,"column":102},"action":"remove","lines":["irst_file_name"],"id":273},{"start":{"row":29,"column":88},"end":{"row":29,"column":89},"action":"insert","lines":["h"]},{"start":{"row":29,"column":89},"end":{"row":29,"column":90},"action":"insert","lines":["o"]},{"start":{"row":29,"column":90},"end":{"row":29,"column":91},"action":"insert","lines":["t"]},{"start":{"row":29,"column":91},"end":{"row":29,"column":92},"action":"insert","lines":["o"]}],[{"start":{"row":29,"column":87},"end":{"row":29,"column":88},"action":"remove","lines":["f"],"id":274}],[{"start":{"row":29,"column":87},"end":{"row":29,"column":88},"action":"insert","lines":["p"],"id":275}],[{"start":{"row":29,"column":51},"end":{"row":29,"column":64},"action":"remove","lines":["first_file_na"],"id":276},{"start":{"row":29,"column":51},"end":{"row":29,"column":52},"action":"insert","lines":["'"]},{"start":{"row":29,"column":52},"end":{"row":29,"column":53},"action":"insert","lines":["m"]},{"start":{"row":29,"column":53},"end":{"row":29,"column":54},"action":"insert","lines":["e"]},{"start":{"row":29,"column":54},"end":{"row":29,"column":55},"action":"insert","lines":["d"]},{"start":{"row":29,"column":55},"end":{"row":29,"column":56},"action":"insert","lines":["i"]}],[{"start":{"row":29,"column":56},"end":{"row":29,"column":57},"action":"insert","lines":["a"],"id":277},{"start":{"row":29,"column":57},"end":{"row":29,"column":58},"action":"insert","lines":["/"]},{"start":{"row":29,"column":58},"end":{"row":29,"column":59},"action":"insert","lines":["'"]}],[{"start":{"row":29,"column":7},"end":{"row":29,"column":8},"action":"insert","lines":[" "],"id":278}],[{"start":{"row":28,"column":45},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":279},{"start":{"row":29,"column":0},"end":{"row":29,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"insert","lines":["f"],"id":280},{"start":{"row":29,"column":9},"end":{"row":29,"column":10},"action":"insert","lines":["i"]},{"start":{"row":29,"column":10},"end":{"row":29,"column":11},"action":"insert","lines":["l"]},{"start":{"row":29,"column":11},"end":{"row":29,"column":12},"action":"insert","lines":["e"]},{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"insert","lines":["n"]},{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"insert","lines":["a"]},{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"insert","lines":["m"]},{"start":{"row":29,"column":15},"end":{"row":29,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"insert","lines":["-"],"id":281}],[{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"remove","lines":["-"],"id":282}],[{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"insert","lines":["="],"id":283}],[{"start":{"row":29,"column":17},"end":{"row":29,"column":19},"action":"insert","lines":["''"],"id":284}],[{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"insert","lines":["{"],"id":285},{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"insert","lines":["}"]}],[{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"remove","lines":["}"],"id":286}],[{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"insert","lines":["}"],"id":287}],[{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["."],"id":288},{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"insert","lines":["f"]},{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"insert","lines":["o"]},{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"insert","lines":["r"]},{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"insert","lines":["m"]},{"start":{"row":29,"column":26},"end":{"row":29,"column":27},"action":"insert","lines":["a"]},{"start":{"row":29,"column":27},"end":{"row":29,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":29,"column":28},"end":{"row":29,"column":30},"action":"insert","lines":["()"],"id":289}],[{"start":{"row":29,"column":29},"end":{"row":29,"column":30},"action":"insert","lines":["p"],"id":290},{"start":{"row":29,"column":30},"end":{"row":29,"column":31},"action":"insert","lines":["g"]}],[{"start":{"row":29,"column":30},"end":{"row":29,"column":31},"action":"remove","lines":["g"],"id":291}],[{"start":{"row":29,"column":30},"end":{"row":29,"column":31},"action":"insert","lines":["h"],"id":292},{"start":{"row":29,"column":31},"end":{"row":29,"column":32},"action":"insert","lines":["o"]},{"start":{"row":29,"column":32},"end":{"row":29,"column":33},"action":"insert","lines":["t"]},{"start":{"row":29,"column":33},"end":{"row":29,"column":34},"action":"insert","lines":["o"]}],[{"start":{"row":30,"column":83},"end":{"row":30,"column":88},"action":"remove","lines":["photo"],"id":296},{"start":{"row":30,"column":83},"end":{"row":30,"column":91},"action":"insert","lines":["filename"]}],[{"start":{"row":30,"column":59},"end":{"row":30,"column":60},"action":"remove","lines":["'"],"id":297},{"start":{"row":30,"column":58},"end":{"row":30,"column":59},"action":"remove","lines":["/"]},{"start":{"row":30,"column":57},"end":{"row":30,"column":58},"action":"remove","lines":["a"]},{"start":{"row":30,"column":56},"end":{"row":30,"column":57},"action":"remove","lines":["i"]},{"start":{"row":30,"column":55},"end":{"row":30,"column":56},"action":"remove","lines":["d"]},{"start":{"row":30,"column":54},"end":{"row":30,"column":55},"action":"remove","lines":["e"]},{"start":{"row":30,"column":53},"end":{"row":30,"column":54},"action":"remove","lines":["m"]},{"start":{"row":30,"column":52},"end":{"row":30,"column":53},"action":"remove","lines":["'"]},{"start":{"row":30,"column":51},"end":{"row":30,"column":52},"action":"remove","lines":[" "]},{"start":{"row":30,"column":50},"end":{"row":30,"column":51},"action":"remove","lines":[","]}],[{"start":{"row":30,"column":52},"end":{"row":30,"column":82},"action":"remove","lines":["upload_file(Filename=filename)"],"id":298},{"start":{"row":30,"column":52},"end":{"row":30,"column":113},"action":"insert","lines":[".upload_file('images/image_0.jpg', 'mybucket', 'image_0.jpg')"]}],[{"start":{"row":30,"column":51},"end":{"row":30,"column":52},"action":"remove","lines":["."],"id":299},{"start":{"row":30,"column":50},"end":{"row":30,"column":51},"action":"remove","lines":[")"]},{"start":{"row":30,"column":49},"end":{"row":30,"column":50},"action":"remove","lines":["E"]},{"start":{"row":30,"column":48},"end":{"row":30,"column":49},"action":"remove","lines":["M"]},{"start":{"row":30,"column":47},"end":{"row":30,"column":48},"action":"remove","lines":["A"]},{"start":{"row":30,"column":46},"end":{"row":30,"column":47},"action":"remove","lines":["N"]},{"start":{"row":30,"column":45},"end":{"row":30,"column":46},"action":"remove","lines":["_"]},{"start":{"row":30,"column":44},"end":{"row":30,"column":45},"action":"remove","lines":["T"]},{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"remove","lines":["E"]},{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"remove","lines":["K"]},{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"remove","lines":["C"]},{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"remove","lines":["U"]},{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"remove","lines":["B"]},{"start":{"row":30,"column":38},"end":{"row":30,"column":39},"action":"remove","lines":["_"]},{"start":{"row":30,"column":37},"end":{"row":30,"column":38},"action":"remove","lines":["E"]},{"start":{"row":30,"column":36},"end":{"row":30,"column":37},"action":"remove","lines":["G"]},{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"remove","lines":["A"]},{"start":{"row":30,"column":34},"end":{"row":30,"column":35},"action":"remove","lines":["R"]},{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"remove","lines":["O"]},{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"remove","lines":["T"]},{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"remove","lines":["S"]},{"start":{"row":30,"column":30},"end":{"row":30,"column":31},"action":"remove","lines":["_"]},{"start":{"row":30,"column":29},"end":{"row":30,"column":30},"action":"remove","lines":["S"]},{"start":{"row":30,"column":28},"end":{"row":30,"column":29},"action":"remove","lines":["W"]}],[{"start":{"row":30,"column":27},"end":{"row":30,"column":28},"action":"remove","lines":["A"],"id":300},{"start":{"row":30,"column":26},"end":{"row":30,"column":27},"action":"remove","lines":["("]}],[{"start":{"row":30,"column":39},"end":{"row":30,"column":59},"action":"remove","lines":["'images/image_0.jpg'"],"id":301},{"start":{"row":30,"column":39},"end":{"row":30,"column":91},"action":"insert","lines":["'media/media/images/watermarks/{}'.format(img.image)"]}],[{"start":{"row":30,"column":93},"end":{"row":30,"column":103},"action":"remove","lines":["'mybucket'"],"id":302}],[{"start":{"row":30,"column":92},"end":{"row":30,"column":116},"action":"insert","lines":[" AWS_STORAGE_BUCKET_NAME"],"id":303}],[{"start":{"row":30,"column":82},"end":{"row":30,"column":90},"action":"remove","lines":["mg.image"],"id":304},{"start":{"row":30,"column":81},"end":{"row":30,"column":82},"action":"remove","lines":["i"]}],[{"start":{"row":30,"column":81},"end":{"row":30,"column":82},"action":"insert","lines":["p"],"id":305},{"start":{"row":30,"column":82},"end":{"row":30,"column":83},"action":"insert","lines":["h"]},{"start":{"row":30,"column":83},"end":{"row":30,"column":84},"action":"insert","lines":["o"]},{"start":{"row":30,"column":84},"end":{"row":30,"column":85},"action":"insert","lines":["t"]},{"start":{"row":30,"column":85},"end":{"row":30,"column":86},"action":"insert","lines":["o"]}],[{"start":{"row":15,"column":33},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":306}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":52},"action":"insert","lines":["client = boto3.client('s3', region_name='us-west-2')"],"id":307}],[{"start":{"row":16,"column":40},"end":{"row":16,"column":51},"action":"remove","lines":["'us-west-2'"],"id":308},{"start":{"row":16,"column":40},"end":{"row":16,"column":58},"action":"insert","lines":["AWS_S3_REGION_NAME"]}],[{"start":{"row":16,"column":59},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":309}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":38},"action":"remove","lines":["s3_resource.Object.upload_file"],"id":310}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":26},"action":"insert","lines":["client.upload_file"],"id":311}],[{"start":{"row":32,"column":74},"end":{"row":32,"column":75},"action":"remove","lines":[")"],"id":312},{"start":{"row":32,"column":73},"end":{"row":32,"column":74},"action":"remove","lines":["o"]},{"start":{"row":32,"column":72},"end":{"row":32,"column":73},"action":"remove","lines":["t"]},{"start":{"row":32,"column":71},"end":{"row":32,"column":72},"action":"remove","lines":["o"]},{"start":{"row":32,"column":70},"end":{"row":32,"column":71},"action":"remove","lines":["h"]},{"start":{"row":32,"column":69},"end":{"row":32,"column":70},"action":"remove","lines":["p"]},{"start":{"row":32,"column":68},"end":{"row":32,"column":69},"action":"remove","lines":["("]},{"start":{"row":32,"column":67},"end":{"row":32,"column":68},"action":"remove","lines":["t"]},{"start":{"row":32,"column":66},"end":{"row":32,"column":67},"action":"remove","lines":["a"]},{"start":{"row":32,"column":65},"end":{"row":32,"column":66},"action":"remove","lines":["m"]},{"start":{"row":32,"column":64},"end":{"row":32,"column":65},"action":"remove","lines":["r"]}],[{"start":{"row":32,"column":63},"end":{"row":32,"column":64},"action":"remove","lines":["o"],"id":313},{"start":{"row":32,"column":62},"end":{"row":32,"column":63},"action":"remove","lines":["f"]},{"start":{"row":32,"column":61},"end":{"row":32,"column":62},"action":"remove","lines":["."]},{"start":{"row":32,"column":60},"end":{"row":32,"column":61},"action":"remove","lines":["'"]}],[{"start":{"row":32,"column":60},"end":{"row":32,"column":61},"action":"insert","lines":["'"],"id":314}],[{"start":{"row":32,"column":59},"end":{"row":32,"column":60},"action":"remove","lines":["}"],"id":315},{"start":{"row":32,"column":58},"end":{"row":32,"column":59},"action":"remove","lines":["{"]}],[{"start":{"row":32,"column":58},"end":{"row":32,"column":59},"action":"insert","lines":["g"],"id":316},{"start":{"row":32,"column":59},"end":{"row":32,"column":60},"action":"insert","lines":["u"]},{"start":{"row":32,"column":60},"end":{"row":32,"column":61},"action":"insert","lines":["l"]},{"start":{"row":32,"column":61},"end":{"row":32,"column":62},"action":"insert","lines":["f"]},{"start":{"row":32,"column":62},"end":{"row":32,"column":63},"action":"insert","lines":["_"]},{"start":{"row":32,"column":63},"end":{"row":32,"column":64},"action":"insert","lines":["p"]}],[{"start":{"row":32,"column":64},"end":{"row":32,"column":65},"action":"insert","lines":["o"],"id":317},{"start":{"row":32,"column":65},"end":{"row":32,"column":66},"action":"insert","lines":["r"]},{"start":{"row":32,"column":66},"end":{"row":32,"column":67},"action":"insert","lines":["s"]},{"start":{"row":32,"column":67},"end":{"row":32,"column":68},"action":"insert","lines":["c"]},{"start":{"row":32,"column":68},"end":{"row":32,"column":69},"action":"insert","lines":["h"]},{"start":{"row":32,"column":69},"end":{"row":32,"column":70},"action":"insert","lines":["e"]}],[{"start":{"row":32,"column":70},"end":{"row":32,"column":71},"action":"insert","lines":["."],"id":318},{"start":{"row":32,"column":71},"end":{"row":32,"column":72},"action":"insert","lines":["j"]},{"start":{"row":32,"column":72},"end":{"row":32,"column":73},"action":"insert","lines":["p"]},{"start":{"row":32,"column":73},"end":{"row":32,"column":74},"action":"insert","lines":["g"]}],[{"start":{"row":67,"column":15},"end":{"row":67,"column":116},"action":"remove","lines":["'https://tidders2000-sharemypics.s3.amazonaws.com/media/media/images/watermarks/{}'.format(img.image)"],"id":319}],[{"start":{"row":67,"column":15},"end":{"row":67,"column":67},"action":"insert","lines":["'media/media/images/watermarks/{}'.format(img.image)"],"id":320}],[{"start":{"row":67,"column":21},"end":{"row":67,"column":22},"action":"remove","lines":["/"],"id":321},{"start":{"row":67,"column":20},"end":{"row":67,"column":21},"action":"remove","lines":["a"]},{"start":{"row":67,"column":19},"end":{"row":67,"column":20},"action":"remove","lines":["i"]},{"start":{"row":67,"column":18},"end":{"row":67,"column":19},"action":"remove","lines":["d"]},{"start":{"row":67,"column":17},"end":{"row":67,"column":18},"action":"remove","lines":["e"]},{"start":{"row":67,"column":16},"end":{"row":67,"column":17},"action":"remove","lines":["m"]}],[{"start":{"row":32,"column":103},"end":{"row":32,"column":104},"action":"insert","lines":["m"],"id":322},{"start":{"row":32,"column":104},"end":{"row":32,"column":105},"action":"insert","lines":["d"]},{"start":{"row":32,"column":105},"end":{"row":32,"column":106},"action":"insert","lines":["e"]}],[{"start":{"row":32,"column":105},"end":{"row":32,"column":106},"action":"remove","lines":["e"],"id":323},{"start":{"row":32,"column":104},"end":{"row":32,"column":105},"action":"remove","lines":["d"]},{"start":{"row":32,"column":103},"end":{"row":32,"column":104},"action":"remove","lines":["m"]}],[{"start":{"row":32,"column":62},"end":{"row":32,"column":63},"action":"remove","lines":["_"],"id":324}],[{"start":{"row":32,"column":62},"end":{"row":32,"column":63},"action":"insert","lines":[" "],"id":325}],[{"start":{"row":32,"column":69},"end":{"row":32,"column":70},"action":"remove","lines":["e"],"id":326},{"start":{"row":32,"column":68},"end":{"row":32,"column":69},"action":"remove","lines":["h"]},{"start":{"row":32,"column":67},"end":{"row":32,"column":68},"action":"remove","lines":["c"]},{"start":{"row":32,"column":66},"end":{"row":32,"column":67},"action":"remove","lines":["s"]},{"start":{"row":32,"column":65},"end":{"row":32,"column":66},"action":"remove","lines":["r"]},{"start":{"row":32,"column":64},"end":{"row":32,"column":65},"action":"remove","lines":["o"]},{"start":{"row":32,"column":63},"end":{"row":32,"column":64},"action":"remove","lines":["p"]},{"start":{"row":32,"column":62},"end":{"row":32,"column":63},"action":"remove","lines":[" "]},{"start":{"row":32,"column":61},"end":{"row":32,"column":62},"action":"remove","lines":["f"]},{"start":{"row":32,"column":60},"end":{"row":32,"column":61},"action":"remove","lines":["l"]}],[{"start":{"row":32,"column":59},"end":{"row":32,"column":60},"action":"remove","lines":["u"],"id":327}],[{"start":{"row":32,"column":58},"end":{"row":32,"column":59},"action":"remove","lines":["g"],"id":328}],[{"start":{"row":32,"column":58},"end":{"row":32,"column":59},"action":"insert","lines":["m"],"id":329},{"start":{"row":32,"column":59},"end":{"row":32,"column":60},"action":"insert","lines":["o"]},{"start":{"row":32,"column":60},"end":{"row":32,"column":61},"action":"insert","lines":["t"]},{"start":{"row":32,"column":61},"end":{"row":32,"column":62},"action":"insert","lines":["o"]}],[{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"remove","lines":["'"],"id":330},{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"remove","lines":["G"]},{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"remove","lines":["E"]},{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"remove","lines":["P"]},{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"remove","lines":["J"]},{"start":{"row":30,"column":38},"end":{"row":30,"column":39},"action":"remove","lines":["'"]},{"start":{"row":30,"column":37},"end":{"row":30,"column":38},"action":"remove","lines":[" "]},{"start":{"row":30,"column":36},"end":{"row":30,"column":37},"action":"remove","lines":[","]}],[{"start":{"row":31,"column":8},"end":{"row":31,"column":35},"action":"remove","lines":["filename='{}'.format(photo)"],"id":331}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":109},"action":"remove","lines":["client.upload_file('media/media/images/watermarks/moto.jpg', AWS_STORAGE_BUCKET_NAME , 'image_0.jpg')"],"id":332}],[{"start":{"row":68,"column":78},"end":{"row":69,"column":0},"action":"insert","lines":["",""],"id":333},{"start":{"row":69,"column":0},"end":{"row":69,"column":10},"action":"insert","lines":["          "]}],[{"start":{"row":69,"column":10},"end":{"row":69,"column":111},"action":"insert","lines":["client.upload_file('media/media/images/watermarks/moto.jpg', AWS_STORAGE_BUCKET_NAME , 'image_0.jpg')"],"id":334}],[{"start":{"row":69,"column":29},"end":{"row":69,"column":69},"action":"remove","lines":["'media/media/images/watermarks/moto.jpg'"],"id":335},{"start":{"row":69,"column":29},"end":{"row":69,"column":30},"action":"insert","lines":["v"]},{"start":{"row":69,"column":30},"end":{"row":69,"column":31},"action":"insert","lines":["a"]},{"start":{"row":69,"column":31},"end":{"row":69,"column":32},"action":"insert","lines":["r"]}],[{"start":{"row":69,"column":61},"end":{"row":69,"column":73},"action":"remove","lines":["image_0.jpg'"],"id":336},{"start":{"row":69,"column":60},"end":{"row":69,"column":61},"action":"remove","lines":["'"]}],[{"start":{"row":69,"column":60},"end":{"row":69,"column":61},"action":"insert","lines":["i"],"id":337},{"start":{"row":69,"column":61},"end":{"row":69,"column":62},"action":"insert","lines":["m"]},{"start":{"row":69,"column":62},"end":{"row":69,"column":63},"action":"insert","lines":["g"]},{"start":{"row":69,"column":63},"end":{"row":69,"column":64},"action":"insert","lines":["."]},{"start":{"row":69,"column":64},"end":{"row":69,"column":65},"action":"insert","lines":["i"]},{"start":{"row":69,"column":65},"end":{"row":69,"column":66},"action":"insert","lines":["m"]},{"start":{"row":69,"column":66},"end":{"row":69,"column":67},"action":"insert","lines":["a"]},{"start":{"row":69,"column":67},"end":{"row":69,"column":68},"action":"insert","lines":["a"]},{"start":{"row":69,"column":68},"end":{"row":69,"column":69},"action":"insert","lines":["g"]}],[{"start":{"row":69,"column":69},"end":{"row":69,"column":70},"action":"insert","lines":["e"],"id":338}],[{"start":{"row":69,"column":65},"end":{"row":69,"column":66},"action":"remove","lines":["m"],"id":339}],[{"start":{"row":69,"column":65},"end":{"row":69,"column":66},"action":"insert","lines":["m"],"id":340}],[{"start":{"row":69,"column":66},"end":{"row":69,"column":67},"action":"remove","lines":["a"],"id":341}],[{"start":{"row":69,"column":29},"end":{"row":69,"column":32},"action":"remove","lines":["var"],"id":342},{"start":{"row":69,"column":29},"end":{"row":69,"column":30},"action":"insert","lines":["'"]}],[{"start":{"row":69,"column":30},"end":{"row":69,"column":60},"action":"insert","lines":["media/media/images/watermarks/"],"id":343}],[{"start":{"row":69,"column":60},"end":{"row":69,"column":61},"action":"insert","lines":["'"],"id":344}],[{"start":{"row":67,"column":16},"end":{"row":67,"column":42},"action":"remove","lines":["media/images/watermarks/{}"],"id":345},{"start":{"row":67,"column":16},"end":{"row":67,"column":84},"action":"insert","lines":["https://tidders2000-sharemypics.s3.amazonaws.com/media/media/images/"]}],[{"start":{"row":67,"column":84},"end":{"row":67,"column":85},"action":"insert","lines":["{"],"id":346},{"start":{"row":67,"column":85},"end":{"row":67,"column":86},"action":"insert","lines":["}"]}],[{"start":{"row":69,"column":60},"end":{"row":69,"column":88},"action":"insert","lines":["images/{}'.format(img.image)"],"id":347}],[{"start":{"row":69,"column":88},"end":{"row":69,"column":89},"action":"remove","lines":["'"],"id":348}],[{"start":{"row":69,"column":116},"end":{"row":69,"column":125},"action":"remove","lines":["img.image"],"id":349}],[{"start":{"row":69,"column":116},"end":{"row":69,"column":156},"action":"insert","lines":["media/media/images/{}'.format(img.image)"],"id":350}],[{"start":{"row":69,"column":116},"end":{"row":69,"column":117},"action":"insert","lines":["'"],"id":351}],[{"start":{"row":69,"column":65},"end":{"row":69,"column":66},"action":"remove","lines":["s"],"id":352},{"start":{"row":69,"column":64},"end":{"row":69,"column":65},"action":"remove","lines":["e"]},{"start":{"row":69,"column":63},"end":{"row":69,"column":64},"action":"remove","lines":["g"]},{"start":{"row":69,"column":62},"end":{"row":69,"column":63},"action":"remove","lines":["a"]},{"start":{"row":69,"column":61},"end":{"row":69,"column":62},"action":"remove","lines":["m"]},{"start":{"row":69,"column":60},"end":{"row":69,"column":61},"action":"remove","lines":["i"]},{"start":{"row":69,"column":59},"end":{"row":69,"column":60},"action":"remove","lines":["/"]}],[{"start":{"row":69,"column":129},"end":{"row":69,"column":130},"action":"insert","lines":["w"],"id":353},{"start":{"row":69,"column":130},"end":{"row":69,"column":131},"action":"insert","lines":["a"]},{"start":{"row":69,"column":131},"end":{"row":69,"column":132},"action":"insert","lines":["t"]},{"start":{"row":69,"column":132},"end":{"row":69,"column":133},"action":"insert","lines":["e"]},{"start":{"row":69,"column":133},"end":{"row":69,"column":134},"action":"insert","lines":["r"]},{"start":{"row":69,"column":134},"end":{"row":69,"column":135},"action":"insert","lines":["m"]},{"start":{"row":69,"column":135},"end":{"row":69,"column":136},"action":"insert","lines":["a"]},{"start":{"row":69,"column":136},"end":{"row":69,"column":137},"action":"insert","lines":["r"]},{"start":{"row":69,"column":137},"end":{"row":69,"column":138},"action":"insert","lines":["k"]},{"start":{"row":69,"column":138},"end":{"row":69,"column":139},"action":"insert","lines":["s"]}],[{"start":{"row":67,"column":84},"end":{"row":67,"column":85},"action":"insert","lines":["w"],"id":354},{"start":{"row":67,"column":85},"end":{"row":67,"column":86},"action":"insert","lines":["a"]},{"start":{"row":67,"column":86},"end":{"row":67,"column":87},"action":"insert","lines":["t"]},{"start":{"row":67,"column":87},"end":{"row":67,"column":88},"action":"insert","lines":["e"]},{"start":{"row":67,"column":88},"end":{"row":67,"column":89},"action":"insert","lines":["r"]},{"start":{"row":67,"column":89},"end":{"row":67,"column":90},"action":"insert","lines":["m"]},{"start":{"row":67,"column":90},"end":{"row":67,"column":91},"action":"insert","lines":["a"]},{"start":{"row":67,"column":91},"end":{"row":67,"column":92},"action":"insert","lines":["r"]},{"start":{"row":67,"column":92},"end":{"row":67,"column":93},"action":"insert","lines":["k"]},{"start":{"row":67,"column":93},"end":{"row":67,"column":94},"action":"insert","lines":["s"]}],[{"start":{"row":67,"column":94},"end":{"row":67,"column":95},"action":"insert","lines":["/"],"id":355}],[{"start":{"row":69,"column":139},"end":{"row":69,"column":140},"action":"insert","lines":["/"],"id":356}],[{"start":{"row":67,"column":16},"end":{"row":67,"column":70},"action":"remove","lines":["https://tidders2000-sharemypics.s3.amazonaws.com/media"],"id":357}],[{"start":{"row":67,"column":16},"end":{"row":67,"column":17},"action":"remove","lines":["/"],"id":359}]]},"ace":{"folds":[],"scrolltop":720,"scrollleft":0,"selection":{"start":{"row":75,"column":48},"end":{"row":75,"column":48},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":50,"state":"start","mode":"ace/mode/python"}},"timestamp":1567606877726,"hash":"ba47c1090514297c2c0d819b9f330b9a42a2fb85"}