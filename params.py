import generateProxy

city_dict = {
    '安庆': {'city_id': '340800', 'max_lat': '30.761368', 'min_lat': '30.310468', 'max_lng': '118.081783',
           'min_lng': '115.874108'},
    # '滁州': {'city_id': '310000', 'max_lat': '31.36552', 'min_lat': '31.106158', 'max_lng': '121.600985',
    #        'min_lng': '121.360095'}, ## 无二手房
    '合肥': {'city_id': '340100', 'max_lat': '32.095428', 'min_lat': '31.65092', 'max_lng': '118.513203',
           'min_lng': '116.305527'},
    '马鞍山': {'city_id': '340500', 'max_lat': '31.921043', 'min_lat': '31.475686', 'max_lng': '119.577175',
            'min_lng': '117.369499'},
    '芜湖': {'city_id': '340200', 'max_lat': '31.62384', 'min_lat': '31.177045', 'max_lng': '119.687577',
           'min_lng': '117.479901'},

    '北京': {'city_id': '110000', 'max_lat': '40.074766', 'min_lat': '39.609408', 'max_lng': '116.796856',
           'min_lng': '115.980476'},

    '重庆': {'city_id': '500000', 'max_lat': '29.832772', 'min_lat': '29.377567', 'max_lng': '107.701369',
           'min_lng': '105.493693'},

    '福州': {'city_id': '350100', 'max_lat': '26.122284', 'min_lat': '26.063489', 'max_lng': '119.603576',
           'min_lng': '119.327616'},
    '泉州': {'city_id': '350500', 'max_lat': '25.153687', 'min_lat': '24.678647', 'max_lng': '119.790306',
           'min_lng': '117.582631'},
    '厦门': {'city_id': '350200', 'max_lat': '24.730621', 'min_lat': '24.253944', 'max_lng': '119.25604',
           'min_lng': '117.048364'},
    '漳州': {'city_id': '350600', 'max_lat': '24.798196', 'min_lat': '24.321779', 'max_lng': '118.681528',
           'min_lng': '116.473852'},

    '东莞': {'city_id': '441900', 'max_lat': '23.261518', 'min_lat': '22.779358', 'max_lng': '114.608143',
           'min_lng': '112.400468'},
    '佛山': {'city_id': '440600', 'max_lat': '23.344281', 'min_lat': '22.69288', 'max_lng': '113.938565',
           'min_lng': '111.730889'},
    '广州': {'city_id': '440100', 'max_lat': '23.296086', 'min_lat': '22.737277', 'max_lng': '113.773905',
           'min_lng': '113.038013'},
    '惠州': {'city_id': '441300', 'max_lat': '23.271555', 'min_lat': '22.56107', 'max_lng': '115.461857',
           'min_lng': '113.254182'},
    '江门': {'city_id': '440700', 'max_lat': '22.828649', 'min_lat': '22.41124', 'max_lng': '114.048661',
           'min_lng': '111.840985'},
    '清远': {'city_id': '441800', 'max_lat': '23.995756', 'min_lat': '23.582024', 'max_lng': '114.155954',
           'min_lng': '111.948279'},
    '深圳': {'city_id': '440300', 'max_lat': '22.935891', 'min_lat': '22.375581', 'max_lng': '114.533683',
           'min_lng': '113.797791'},
    '珠海': {'city_id': '440400', 'max_lat': '22.531309', 'min_lat': '21.818023', 'max_lng': '114.422509',
           'min_lng': '112.214833'},
    '湛江': {'city_id': '440800', 'max_lat': '21.440457', 'min_lat': '21.13007', 'max_lng': '111.444095',
           'min_lng': '109.23642'},
    '中山': {'city_id': '442000', 'max_lat': '22.772602', 'min_lat': '22.224467', 'max_lng': '114.41817',
           'min_lng': '112.210495'},

    '北海': {'city_id': '450500', 'max_lat': '21.920169', 'min_lat': '21.368671', 'max_lng': '110.183226',
           'min_lng': '107.97555'},
    '防城港': {'city_id': '450600', 'max_lat': '21.992257', 'min_lat': '21.441038', 'max_lng': '109.282585',
            'min_lng': '107.074909'},
    '桂林': {'city_id': '450300', 'max_lat': '25.546957', 'min_lat': '25.010609', 'max_lng': '111.318208',
           'min_lng': '109.110532'},
    '柳州': {'city_id': '450200', 'max_lat': '24.624262', 'min_lat': '24.083852', 'max_lng': '110.645197',
           'min_lng': '108.437521'},
    '南宁': {'city_id': '450100', 'max_lat': '23.124728', 'min_lat': '22.578018', 'max_lng': '109.544557',
           'min_lng': '107.336881'},

    '兰州': {'city_id': '620100', 'max_lat': '36.410731', 'min_lat': '35.93245', 'max_lng': '104.762114',
           'min_lng': '102.554438'},

    '贵阳': {'city_id': '520100', 'max_lat': '26.919842', 'min_lat': '26.3898', 'max_lng': '107.699599',
           'min_lng': '105.491923'},

    '保定': {'city_id': '130600', 'max_lat': '39.106794', 'min_lat': '38.645689', 'max_lng': '116.415471',
           'min_lng': '114.207796'},
    '廊坊': {'city_id': '131000', 'max_lat': '39.809267', 'min_lat': '39.352807', 'max_lng': '117.790965',
           'min_lng': '115.58329'},
    # '秦皇岛': {'city_id': '450100', 'max_lat': '23', 'min_lat': '22', 'max_lng': '109',
    #         'min_lng': '107'},
    '石家庄': {'city_id': '130100', 'max_lat': '38.355913', 'min_lat': '37.845253', 'max_lng': '115.662736',
            'min_lng': '113.455061'},
    '唐山': {'city_id': '130200', 'max_lat': '39.909872', 'min_lat': '39.41039', 'max_lng': '119.240858',
           'min_lng': '117.033182'},
    '张家口': {'city_id': '130700', 'max_lat': '41.040191', 'min_lat': '40.549071', 'max_lng': '116.068276',
            'min_lng': '113.860601'},

    '海口': {'city_id': '460100', 'max_lat': '20.29487', 'min_lat': '19.683944', 'max_lng': '111.348301',
           'min_lng': '109.140625'},
    '三亚': {'city_id': '460200', 'max_lat': '18.672424', 'min_lat': '18.055366', 'max_lng': '110.512589',
           'min_lng': '108.304913'},

    '长沙': {'city_id': '430100', 'max_lat': '28.368467', 'min_lat': '28.101143', 'max_lng': '113.155889',
           'min_lng': '112.735051'},
    '常德': {'city_id': '430700', 'max_lat': '29.306702', 'min_lat': '28.738702', 'max_lng': '112.659809',
           'min_lng': '110.452133'},
    '岳阳': {'city_id': '430600', 'max_lat': '29.621217', 'min_lat': '29.054979', 'max_lng': '114.0726',
           'min_lng': '111.864925'},
    '株洲': {'city_id': '430200', 'max_lat': '28.119408', 'min_lat': '27.544915', 'max_lng': '114.263859',
           'min_lng': '112.056183'},

    '开封': {'city_id': '410200', 'max_lat': '35.065666', 'min_lat': '34.53545', 'max_lng': '115.259181',
           'min_lng': '113.051506'},
    '洛阳': {'city_id': '410300', 'max_lat': '34.914383', 'min_lat': '34.383183', 'max_lng': '113.513819',
           'min_lng': '111.306143'},
    '新乡': {'city_id': '410700', 'max_lat': '35.600598', 'min_lat': '35.073889', 'max_lng': '114.931075',
           'min_lng': '112.7234'},
    '许昌': {'city_id': '411000', 'max_lat': '34.33217', 'min_lat': '33.797221', 'max_lng': '114.761664',
           'min_lng': '112.553989'},
    '郑州': {'city_id': '410100', 'max_lat': '34.961967', 'min_lat': '34.473941', 'max_lng': '113.50206',
           'min_lng': '112.899549'},
    '周口': {'city_id': '411600', 'max_lat': '33.912671', 'min_lat': '33.375055', 'max_lng': '116.07743',
           'min_lng': '113.869754'},
    # '驻马店': {'city_id': '411700', 'max_lat': '33.338634', 'min_lat': '32.835284', 'max_lng': '115.234065',
    #         'min_lng': '113.026389'}, ##城市未开通

    '鄂州': {'city_id': '420700', 'max_lat': '30.62109', 'min_lat': '30.102566', 'max_lng': '115.658775',
           'min_lng': '113.451099'},
    '黄石': {'city_id': '420200', 'max_lat': '30.433161', 'min_lat': '29.913631', 'max_lng': '115.924575',
           'min_lng': '113.716899'},
    '武汉': {'city_id': '420100', 'max_lat': '30.836902', 'min_lat': '30.319541', 'max_lng': '115.206155',
           'min_lng': '112.998479'},
    '襄阳': {'city_id': '420600', 'max_lat': '32.29066', 'min_lat': '31.781322', 'max_lng': '112.959286',
           'min_lng': '110.75161'},
    '宜昌': {'city_id': '420500', 'max_lat': '30.95942', 'min_lat': '30.442722', 'max_lng': '112.266459',
           'min_lng': '110.058783'},

    '哈尔滨': {'city_id': '230100', 'max_lat': '45.946361', 'min_lat': '45.453258', 'max_lng': '127.807575',
            'min_lng': '125.599899'},

    '赣州': {'city_id': '360700', 'max_lat': '26.133452', 'min_lat': '25.538225', 'max_lng': '116.300758',
           'min_lng': '114.093083'},
    '九江': {'city_id': '360400', 'max_lat': '29.932431', 'min_lat': '29.357879', 'max_lng': '117.045525',
           'min_lng': '114.837849'},
    '吉安': {'city_id': '360800', 'max_lat': '27.303754', 'min_lat': '26.742497', 'max_lng': '116.008916',
           'min_lng': '113.80124'},
    '南昌': {'city_id': '360100', 'max_lat': '28.960587', 'min_lat': '28.407954', 'max_lng': '116.900008',
           'min_lng': '114.692332'},
    '上饶': {'city_id': '361100', 'max_lat': '28.785048', 'min_lat': '28.231479', 'max_lng': '119.201054',
           'min_lng': '116.993378'},

    '常州': {'city_id': '320400', 'max_lat': '32.080272', 'min_lat': '31.545136', 'max_lng': '120.973788',
           'min_lng': '118.766113'},
    '南京': {'city_id': '320100', 'max_lat': '32.340119', 'min_lat': '31.806513', 'max_lng': '119.990197',
           'min_lng': '117.782522'},
    '淮安': {'city_id': '320800', 'max_lat': '33.831806', 'min_lat': '33.307198', 'max_lng': '120.060903',
           'min_lng': '117.853227'},
    '南通': {'city_id': '320600', 'max_lat': '32.333062', 'min_lat': '31.799415', 'max_lng': '122.077868',
           'min_lng': '119.870193'},
    '苏州': {'city_id': '320500', 'max_lat': '31.530621', 'min_lat': '30.992285', 'max_lng': '121.718671',
           'min_lng': '119.510996'},
    '无锡': {'city_id': '320200', 'max_lat': '31.787286', 'min_lat': '31.250438', 'max_lng': '121.28674',
           'min_lng': '119.079064'},
    '徐州': {'city_id': '320300', 'max_lat': '34.532312', 'min_lat': '34.012053', 'max_lng': '118.282878',
           'min_lng': '116.075203'},
    '盐城': {'city_id': '320900', 'max_lat': '33.812493', 'min_lat': '33.287766', 'max_lng': '120.861464',
           'min_lng': '118.653788'},
    '镇江': {'city_id': '321100', 'max_lat': '32.347122', 'min_lat': '31.813558', 'max_lng': '120.425381',
           'min_lng': '118.217706'},

    '长春': {'city_id': '220100', 'max_lat': '44.119047', 'min_lat': '43.665856', 'max_lng': '126.548852',
           'min_lng': '124.341176'},
    '吉林': {'city_id': '220200', 'max_lat': '44.113218', 'min_lat': '43.659982', 'max_lng': '127.620378',
           'min_lng': '125.412702'},

    '大连': {'city_id': '210200', 'max_lat': '39.171146', 'min_lat': '38.681628', 'max_lng': '122.635204',
           'min_lng': '120.427528'},
    '丹东': {'city_id': '210600', 'max_lat': '40.252006', 'min_lat': '39.770121', 'max_lng': '125.383175',
           'min_lng': '123.175499'},
    '沈阳': {'city_id': '210100', 'max_lat': '41.920222', 'min_lat': '41.450453', 'max_lng': '124.584706',
           'min_lng': '122.377031'},

    '包头': {'city_id': '150200', 'max_lat': '40.910923', 'min_lat': '40.433775', 'max_lng': '110.903235',
           'min_lng': '108.695559'},
    '赤峰': {'city_id': '150400', 'max_lat': '42.531653', 'min_lat': '42.066426', 'max_lng': '120.13734',
           'min_lng': '117.929664'},
    '呼和浩特': {'city_id': '150100', 'max_lat': '41.132243', 'min_lat': '40.6567', 'max_lng': '112.842102',
             'min_lng': '110.634427'},

    '银川': {'city_id': '640100', 'max_lat': '38.729519', 'min_lat': '38.236933', 'max_lng': '107.179058',
           'min_lng': '104.971382'},

    '菏泽': {'city_id': '371700', 'max_lat': '35.519811', 'min_lat': '35.005816', 'max_lng': '116.475254',
           'min_lng': '114.267578'},
    '济南': {'city_id': '370101', 'max_lat': '36.929604', 'min_lat': '36.424817', 'max_lng': '118.27968',
           'min_lng': '116.072004'},
    '济宁': {'city_id': '370800', 'max_lat': '35.702291', 'min_lat': '35.18947', 'max_lng': '117.547399',
           'min_lng': '115.339723'},
    '临沂': {'city_id': '371300', 'max_lat': '35.391525', 'min_lat': '34.876708', 'max_lng': '119.426556',
           'min_lng': '117.21888'},
    '青岛': {'city_id': '370200', 'max_lat': '36.348756', 'min_lat': '35.840137', 'max_lng': '121.345542',
           'min_lng': '119.137867'},
    '泰安': {'city_id': '370900', 'max_lat': '36.441041', 'min_lat': '35.933027', 'max_lng': '118.213278',
           'min_lng': '116.005602'},
    '潍坊': {'city_id': '370700', 'max_lat': '36.971661', 'min_lat': '36.467153', 'max_lng': '120.18195',
           'min_lng': '117.974274'},
    '威海': {'city_id': '371000', 'max_lat': '37.550999', 'min_lat': '37.050368', 'max_lng': '123.027863',
           'min_lng': '120.820187'},
    '烟台': {'city_id': '370600', 'max_lat': '37.590234', 'min_lat': '37.349651', 'max_lng': '121.698469',
           'min_lng': '121.210365'},
    '淄博': {'city_id': '370300', 'max_lat': '37.043635', 'min_lat': '36.539606', 'max_lng': '118.933602',
           'min_lng': '116.725926'},

    '巴中': {'city_id': '511900', 'max_lat': '32.080924', 'min_lat': '31.545791', 'max_lng': '108.06009',
           'min_lng': '105.852414'},
    '成都': {'city_id': '510100', 'max_lat': '30.846502', 'min_lat': '30.304253', 'max_lng': '105.197855',
           'min_lng': '102.990179'},
    '德阳': {'city_id': '510600', 'max_lat': '31.444563', 'min_lat': '30.90573', 'max_lng': '105.527771',
           'min_lng': '103.320095'},
    '达州': {'city_id': '511700', 'max_lat': '31.505148', 'min_lat': '30.966664', 'max_lng': '108.426652',
           'min_lng': '106.218976'},
    '广元': {'city_id': '510800', 'max_lat': '32.709122', 'min_lat': '32.177709', 'max_lng': '106.8272',
           'min_lng': '104.619525'},
    '凉山': {'city_id': '513400', 'max_lat': '28.143128', 'min_lat': '27.586182', 'max_lng': '103.197391',
           'min_lng': '100.989716'},
    '绵阳': {'city_id': '510700', 'max_lat': '31.723895', 'min_lat': '31.186678', 'max_lng': '105.811819',
           'min_lng': '103.604144'},
    '南充': {'city_id': '511300', 'max_lat': '31.13429', 'min_lat': '30.593677', 'max_lng': '107.175923',
           'min_lng': '104.968248'},
    '遂宁': {'city_id': '510900', 'max_lat': '30.845915', 'min_lat': '30.303662', 'max_lng': '106.791799',
           'min_lng': '104.584123'},
    '宜宾': {'city_id': '511500', 'max_lat': '29.104222', 'min_lat': '28.552359', 'max_lng': '105.599163',
           'min_lng': '103.391488'},

    '宝鸡': {'city_id': '610300', 'max_lat': '34.670386', 'min_lat': '34.150994', 'max_lng': '108.221354',
           'min_lng': '106.013678'},
    '汉中': {'city_id': '610700', 'max_lat': '33.340353', 'min_lat': '32.812741', 'max_lng': '108.082097',
           'min_lng': '105.874422'},
    '西安': {'city_id': '610100', 'max_lat': '34.604144', 'min_lat': '34.084335', 'max_lng': '109.928421',
           'min_lng': '107.720745'},
    '咸阳': {'city_id': '610400', 'max_lat': '34.651324', 'min_lat': '34.131812', 'max_lng': '109.754293',
           'min_lng': '107.546618'},

    '晋中': {'city_id': '140700', 'max_lat': '37.91705', 'min_lat': '37.418895', 'max_lng': '114.054303',
           'min_lng': '111.846627'},
    '太原': {'city_id': '140100', 'max_lat': '38.08655', 'min_lat': '37.589548', 'max_lng': '113.619415',
           'min_lng': '111.411739'},

    '上海': {'city_id': '310000', 'max_lat': '31.36552', 'min_lat': '31.106158', 'max_lng': '121.600985',
           'min_lng': '121.360095'},

    '天津': {'city_id': '120000', 'max_lat': '39.343123', 'min_lat': '38.854808', 'max_lng': '118.129681',
           'min_lng': '115.922005'},

    '大理': {'city_id': '532900', 'max_lat': '25.962227', 'min_lat': '25.394334', 'max_lng': '101.496422',
           'min_lng': '99.288747'},
    '昆明': {'city_id': '530100', 'max_lat': '25.189292', 'min_lat': '24.617719', 'max_lng': '103.842096',
           'min_lng': '101.63442'},

    '杭州': {'city_id': '330100', 'max_lat': '30.519225', 'min_lat': '30.162163', 'max_lng': '121.262786',
           'min_lng': '118.629098'},
    '湖州': {'city_id': '330500', 'max_lat': '31.195232', 'min_lat': '30.708636', 'max_lng': '121.392677',
           'min_lng': '119.185002'},
    '嘉兴': {'city_id': '330400', 'max_lat': '31.067999', 'min_lat': '30.580748', 'max_lng': '121.84324',
           'min_lng': '119.635565'},
    '金华': {'city_id': '330700', 'max_lat': '29.336592', 'min_lat': '28.84067', 'max_lng': '121.241933',
           'min_lng': '119.034257'},
    '宁波': {'city_id': '330200', 'max_lat': '30.094564', 'min_lat': '29.602382', 'max_lng': '122.651894',
           'min_lng': '120.444218'},
    '衢州': {'city_id': '330800', 'max_lat': '29.259032', 'min_lat': '28.762732', 'max_lng': '120.060122',
           'min_lng': '117.852446'},
    '绍兴': {'city_id': '330600', 'max_lat': '30.278941', 'min_lat': '29.787682', 'max_lng': '121.670343',
           'min_lng': '119.462667'},
    '台州': {'city_id': '331000', 'max_lat': '28.926315', 'min_lat': '28.428405', 'max_lng': '122.42836',
           'min_lng': '120.220684'},
    '温州': {'city_id': '330300', 'max_lat': '28.284187', 'min_lat': '27.783216', 'max_lng': '121.690734',
           'min_lng': '119.483059'},
}

direct_city_dict = {
    '北京': {'city_id': '110000', 'max_lat': '40.074766', 'min_lat': '39.609408', 'max_lng': '116.796856',
           'min_lng': '115.980476'},
    '天津': {'city_id': '120000', 'max_lat': '39.343123', 'min_lat': '38.854808', 'max_lng': '118.129681',
           'min_lng': '115.922005'},
    '上海': {'city_id': '310000', 'max_lat': '31.36552', 'min_lat': '31.106158', 'max_lng': '121.600985',
           'min_lng': '121.360095'},
    '南京': {'city_id': '320100', 'max_lat': '32.340119', 'min_lat': '31.806513', 'max_lng': '119.990197',
               'min_lng': '117.782522'},
    '无锡': {'city_id': '320200', 'max_lat': '31.787286', 'min_lat': '31.250438', 'max_lng': '121.28674',
               'min_lng': '119.079064'},
    '苏州': {'city_id': '320500', 'max_lat': '31.530621', 'min_lat': '30.992285', 'max_lng': '121.718671',
               'min_lng': '119.510996'},
    '杭州': {'city_id': '330100', 'max_lat': '30.519225', 'min_lat': '30.162163', 'max_lng': '121.262786',
               'min_lng': '118.629098'},
    '厦门': {'city_id': '350200', 'max_lat': '24.730621', 'min_lat': '24.253944', 'max_lng': '119.25604',
               'min_lng': '117.048364'},
    '青岛': {'city_id': '370200', 'max_lat': '36.348756', 'min_lat': '35.840137', 'max_lng': '121.345542',
               'min_lng': '119.137867'},
    '长沙': {'city_id': '430100', 'max_lat': '28.368467', 'min_lat': '28.101143', 'max_lng': '113.155889',
               'min_lng': '112.735051'},
    '广州': {'city_id': '440100', 'max_lat': '23.296086', 'min_lat': '22.737277', 'max_lng': '113.773905',
               'min_lng': '113.038013'},
    '深圳': {'city_id': '440300', 'max_lat': '22.935891', 'min_lat': '22.375581', 'max_lng': '114.533683',
               'min_lng': '113.797791'},
    '东莞': {'city_id': '441900', 'max_lat': '23.261518', 'min_lat': '22.779358', 'max_lng': '114.608143',
               'min_lng': '112.400468'},
    '重庆': {'city_id': '500000', 'max_lat': '29.832772', 'min_lat': '29.377567', 'max_lng': '107.701369',
               'min_lng': '105.493693'},
    '成都': {'city_id': '510100', 'max_lat': '30.846502', 'min_lat': '30.304253', 'max_lng': '105.197855',
               'min_lng': '102.990179'},
}

url_fang = 'https://ajax.lianjia.com/map/resblock/ershoufanglist/?callback=jQuery11110617424919783834_1541868368031' \
                '&id=%s' \
                '&order=0' \
                '&page=%d' \
                '&filters=%s' \
                '&request_ts=%d' \
                '&source=ljpc' \
                '&authorization=%s' \
                '&_=%d'
url = 'https://ajax.lianjia.com/map/search/ershoufang/?callback=jQuery1111012389114747347363_1534230881479' \
           '&city_id=%s' \
           '&group_type=%s' \
           '&max_lat=%s' \
           '&min_lat=%s' \
           '&max_lng=%s' \
           '&min_lng=%s' \
           '&filters=%s' \
           '&request_ts=%d' \
           '&source=ljpc' \
           '&authorization=%s' \
           '&_=%d'

cookies = {
    'lianjia_uuid': '9bdccc1a-7584-4639-ba95-b42cf21bbbc7',
    'jzqa': '1.3180246719396510700.1534145942.1534145942.1534145942.1',
    'jzqckmp': '1',
    'ga': 'GA1.2.964691746.1534145946',
    'gid': 'GA1.2.826685830.1534145946',
    'UM_distinctid': '165327625186a-029cf60b1994ee-3461790f-fa000-165327625199d3',
    'select_city': '310000',
    'lianjia_ssid': '34fc4efa-7fcc-4f3f-82ae-010401f27aa8',
    '_smt_uid': '5b72c5f7.5815bcdf',
    'Hm_lvt_9152f8221cb6243a53c83b956842be8a': '1537530243',
    '_jzqc': '1',
    '_gid': 'GA1.2.178601063.1541866763',
    '_jzqb': '1.2.10.1541866760.1'
}

headers = {
    'Host': 'ajax.lianjia.com',
    'Referer': 'https://sh.lianjia.com/ditu/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

proxies = generateProxy.generate()

key = '9777f65a7dde829ab293c9db5fdb6ddb'

provinceUrls = {
    "http://www.anjuke.com/fangjia/anhui2020/",
    "http://www.anjuke.com/fangjia/fujian2020/",
    "http://www.anjuke.com/fangjia/gansu2020/",
    "http://www.anjuke.com/fangjia/guangdong2020/",
    "http://www.anjuke.com/fangjia/guangxi2020/",
    "http://www.anjuke.com/fangjia/guizhou2020/",
    "http://www.anjuke.com/fangjia/hainan2020/",
    "http://www.anjuke.com/fangjia/hebei2020/",
    "http://www.anjuke.com/fangjia/heilongjiang2020/",
    "http://www.anjuke.com/fangjia/henan2020/",
    "http://www.anjuke.com/fangjia/hubei2020/",
    "http://www.anjuke.com/fangjia/hunan2020/",
    "http://www.anjuke.com/fangjia/jiangsu2020/",
    "http://www.anjuke.com/fangjia/jiangxi2020/",
    "http://www.anjuke.com/fangjia/jilin2020/",
    "http://www.anjuke.com/fangjia/liaoning2020/",
    "http://www.anjuke.com/fangjia/neimenggu2020/",
    "http://www.anjuke.com/fangjia/ningxia2020/",
    "http://www.anjuke.com/fangjia/qinghai2020/",
    "http://www.anjuke.com/fangjia/shan3xi2020/",
    "http://www.anjuke.com/fangjia/shandong2020/",
    "http://www.anjuke.com/fangjia/shanxi2020/",
    "http://www.anjuke.com/fangjia/sichuan2020/",
    "http://www.anjuke.com/fangjia/xinjiang2020/",
    "http://www.anjuke.com/fangjia/xizang2020/",
    "http://www.anjuke.com/fangjia/yunnan2020/",
    "http://www.anjuke.com/fangjia/zhejiang2020/",
}

anjukeHeaders = {
    'Host': 'www.anjuke.com',
    'Referer': 'https://www.google.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

anjukeCookies = {
    'aQQ_ajkguid': 'C3916F21-95C4-20D0-6A0E-F32C823F8545',
    '58tj_uuid': '2071f94b-ce16-4b87-8d65-14c04ce46807',
    'als': '0',
    'id58': 'e87rkF7LOj+/qxdZA4yfAg==',
    'isp': 'true',
    'Hm_lvt_c5899c8768ebee272710c9c5f365a6d8': '1591584748,1591789829',
    '_ga': 'GA1.2.942347589.1591790560',
    'sessid': '1A11F698-333D-8690-0D52-89E2640E5768',
    'lps': 'http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fwww.google.com%2F',
    'twe': '2',
    'wmda_new_uuid': '1',
    'wmda_uuid': '53bd4b15c7c5d713f4cf047169449cc2',
    'wmda_visited_projects': '%3B6289197098934',
    'ajk_member_captcha': '65ec74234236d95b48e8af6681cb84ee',
    'ctid': '75',
    'wmda_session_id_6289197098934': '1592628931294-34c6f663-4020-a9f5',
    '__xsptplusUT_8': '1',
    'new_session': '1',
    'init_refer': 'https%253A%252F%252Fwww.google.com%252F',
    'new_uv': '12',
    '__xsptplus8': '8.11.1592628931.1592628931.1%233%7Cwww.google.com%7C%7C%7C%7C%23%238uddg2f7w7snTu1PSKJw01mvrnlx1Dkp%23',
    'xxzl_cid': '28e3ee5da25343329010cfb4f86c6217',
    'xzuid': 'a4690306-64be-4898-9f81-b346697cfece'
}


