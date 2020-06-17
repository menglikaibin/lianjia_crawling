
city_dict = {
    '上海': {'city_id': '310000', 'max_lat': '31.36552', 'min_lat': '31.106158', 'max_lng': '121.600985',
           'min_lng': '121.360095'},
    '北京': {'city_id': '110000', 'max_lat': '40.074766', 'min_lat': '39.609408', 'max_lng': '116.796856',
           'min_lng': '115.980476'},
    '广州': {'city_id': '440100', 'max_lat': '23.296086', 'min_lat': '22.737277', 'max_lng': '113.773905',
           'min_lng': '113.038013'},
    '深圳': {'city_id': '440300', 'max_lat': '22.935891', 'min_lat': '22.375581', 'max_lng': '114.533683',
           'min_lng': '113.797791'},
    '长沙': {'city_id': '430100', 'max_lat': '28.368467', 'min_lat': '28.101143', 'max_lng': '113.155889',
           'min_lng': '112.735051'},
    '烟台': {'city_id': '370600', 'max_lat': '37.590234', 'min_lat': '37.349651', 'max_lng': '121.698469',
           'min_lng': '121.210365'},
    '厦门': {'city_id': '350200', 'max_lat': '24.794145', 'min_lat': '24.241819', 'max_lng': '118.533083',
           'min_lng': '117.892627'},
    '郑州': {'city_id': '410100', 'max_lat': '34.961967', 'min_lat': '34.473941', 'max_lng': '113.50206',
           'min_lng': '112.899549'},
    # '杭州': {'city_id': '330100', 'max_lat': '30.266026', 'min_lat': '30.197379', 'max_lng': '120.312738',
    #        'min_lng': '120.036779'}
    '杭州': {'city_id': '330100', 'max_lat': '30.519225', 'min_lat': '30.162163', 'max_lng': '121.262786',
           'min_lng': '118.629098'}
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