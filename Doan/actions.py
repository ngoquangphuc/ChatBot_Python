from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class GetMoTaAction(Action):

    def name(self):
        return "get_mo_ta_action"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        loc = tracker.get_slot('location').capitalize()
        base_url = "https://neu-api.herokuapp.com/{nganh}"
        url = base_url.format(**{'nganh': loc})
        res = requests.get(url)
        moTa = res.json()['Mo ta']
        response = "Doi voi sinh vien {} {}".format(loc, moTa)

        dispatcher.utter_message(response)
        return [SlotSet("location", loc)]

class GetKhoaAction(Action):

    def name(self):
        return "get_khoa_action"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        loc = tracker.get_slot('location').capitalize()
        base_url = "https://neu-api.herokuapp.com/{nganh}"
        url = base_url.format(**{'nganh': loc})
        res = requests.get(url)
        khoa = res.json()['Khoa']
        response = "Nganh {} thuoc {} a.".format(loc, khoa)

        dispatcher.utter_message(response)
        return [SlotSet("location", loc)]
    
class GetMaAction(Action):

    def name(self):
        return "get_ma_action"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        loc = tracker.get_slot('location').capitalize()
        base_url = "https://neu-api.herokuapp.com/{nganh}"
        url = base_url.format(**{'nganh': loc})
        res = requests.get(url)
        ma = res.json()['Ma']
        response = "Nganh {} co ma tuyen sinh la {}".format(loc, ma)

        dispatcher.utter_message(response)
        return [SlotSet("location", loc)]

          
class GetChiTieuAction(Action):

    def name(self):
        return "get_chi_tieu_action"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        loc = tracker.get_slot('location').capitalize()
        base_url = "https://neu-api.herokuapp.com/{nganh}"
        url = base_url.format(**{'nganh': loc})
        res = requests.get(url)
        chiTieu = res.json()['Chi tieu']
        response = "Nganh {} co chi tieu tuyen sinh la {}".format(loc, chiTieu)

        dispatcher.utter_message(response)
        return [SlotSet("location", loc)]

class GetToHopAction(Action):

    def name(self):
        return "get_to_hop_action"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        loc = tracker.get_slot('location').capitalize()
        base_url = "https://neu-api.herokuapp.com/{nganh}"
        url = base_url.format(**{'nganh': loc})
        res = requests.get(url)
        toHop = res.json()['To hop xet tuyen']
        response = "Nganh {} xet tuyen cac khoi {}".format(loc, toHop)

        dispatcher.utter_message(response)
        return [SlotSet("location", loc)]

class GetDiemAction(Action):

    def name(self):
        return "get_diem_action"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        loc = tracker.get_slot('location').capitalize()
        base_url = "https://neu-api.herokuapp.com/{nganh}"
        url = base_url.format(**{'nganh': loc})
        res = requests.get(url)
        diem2015 = res.json()['Diem 2015']
        diem2016 = res.json()['Diem 2016']
        diem2017 = res.json()['Diem 2017']
        diem2018 = res.json()['Diem 2018']
        response = "Nganh {} co diem xet tuyen nam 2015 la: {}, 2016 la: {}, 2017 la: {}, 2018 la: {}. Luu y: Nhung nam co diem xet tuyen  bang 00.00 la nhung nam nha truong chua to chuc tuyen sinh.".format(loc, diem2015, diem2016, diem2017, diem2018)

        dispatcher.utter_message(response)
        return [SlotSet("location", loc)]
          
class GetTinChiAction(Action):

    def name(self):
        return "get_tin_chi_action"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        loc = tracker.get_slot('location').capitalize()
        base_url = "https://neu-api.herokuapp.com/{nganh}"
        url = base_url.format(**{'nganh': loc})
        res = requests.get(url)
        tinChi = res.json()['Tong so tin chi']
        response = "Nganh {} tong so tin chi la: {}".format(loc, tinChi)

        dispatcher.utter_message(response)
        return [SlotSet("location", loc)]

class GetChuongTrinhAction(Action):

    def name(self):
        return "get_chuong_trinh_action"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        loc = tracker.get_slot('location').capitalize()
        base_url = "https://neu-api.herokuapp.com/{nganh}"
        url = base_url.format(**{'nganh': loc})
        res = requests.get(url)
        chuongTrinh = res.json()['Chuong trinh dao tao']
        response = "Nganh {} co {}".format(loc, chuongTrinh)

        dispatcher.utter_message(response)
        return [SlotSet("location", loc)]

class GetCoHoiAction(Action):

    def name(self):
        return "get_co_hoi_action"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        loc = tracker.get_slot('location').capitalize()
        base_url = "https://neu-api.herokuapp.com/{nganh}"
        url = base_url.format(**{'nganh': loc})
        res = requests.get(url)
        coHoi = res.json()['Co hoi nghe nghiep']
        response = "{}".format(coHoi)

        dispatcher.utter_message(response)
        return [SlotSet("location", loc)]
    