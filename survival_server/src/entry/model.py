'''
LivestockHouse
livestockHouse
id 唯一id
temperature 温度
humidness 湿度
food 食物含量
water 水含量
livestockIds 牲畜ids
remark 备注
'''
class LivestockHouse(object):
    def __init__(self,id):
        self.livestockHouse_id = id

    @property
    def id(self):
        return self.livestockHouse_id
    
    @id.setter
    def id(self, id):
        self.livestockHouse_id = id
    #data = {temperature = 32.32, humidness = 23.3, food = 100%, water = 100%, pigIds, remark}

    @property
    def temperature(self):
        return self.livestockHouse_temperature

    @temperature.setter
    def temperature(self, temperature):
        self.livestockHouse_temperature = temperature

    @property
    def humidness(self):
        return self.livestockHouse_humidness
    
    @humidness.setter
    def humidness(self, humidness):
        self.livestockHouse_humidness = humidness


'''
Pigstry
id 唯一id
temperature 温度
humidness 湿度
food 食物含量
water 水含量
pigIds 猪ids
remark 备注
'''
class Pigsty(object):
    
    def __init__(self,id):
        self.pigsty_id = id

    @property
    def id(self):
        return self.pigsty_id
    
    @id.setter
    def id(self, id):
        self.pigsty_id = id
    #data = {temperature = 32.32, humidness = 23.3, food = 100%, water = 100%, pigIds, remark}

    @property
    def temperature(self):
        return self.pigsty_temperature

    @temperature.setter
    def temperature(self, temperature):
        self.pigsty_temperature = temperature

    @property
    def humidness(self):
        return self.pigsty_humidness
    
    @humidness.setter
    def humidness(self, humidness):
        self.pigsty_humidness = humidness

    

'''
Pig

'''

