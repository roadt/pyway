import  pytest

from ctext import *
skip=pytest.mark.skip

class TestCText:

    @classmethod
    def setup_class(self):
        #setapikey('')
        #setlanguage("zh")
        #setremap("gb")
        pass

    @skip
    def test_getstats():
        stats = getstats()
        print(stats)

    @skip
    def test_getstats():
        status = getstatus()
        print(status)

    @skip
    def test_gettexttitles():
        titles = gettexttitles()
        print(titles)

    @skip
    def test_getcapabilities():
        capabilities = getcapabilities()
        print(capabilities)

    @skip
    def test_readlink():
        urn = readlink("http://ctext.org/mengzi")
        print(urn)

    @skip
    def test_gettext(self):
        '''Simple wrapper around the gettext API call. Note that the API gettext function needs to be called recursively to get
the full text of an entire book
        the Python helper functions gettextasparagraphlist, gettextasstring, and gettextasobject call gettext repeatedly to extract all corresponding textual data.
        '''
        passages  = gettext("ctp:analects/xue-er")
        print(passages)
        json_data = {'fulltext': ['子曰：「學而時習之，不亦說乎？有朋自遠方來，不亦樂乎？人不知而不慍，不亦君子乎？」', '有子曰：「其為人也孝弟，而好犯上者，鮮矣；不好犯上，而好作亂者，未之有也。君子務本，本立而道生。孝弟也者，其為仁之本與！」', '子曰：「巧言令色，鮮矣仁！」', '曾子曰：「吾日三省吾身：為人謀而不忠乎？與朋友交而不信乎？傳不習乎？」', '子曰：「道千乘之國：敬事而信，節用而愛人，使民以時。」', '子曰：「弟子入則孝，出則弟，謹而信，汎愛眾，而親仁。行有餘力，則以學文。」', '子夏曰：「賢賢易色，事父母能竭其力，事君能致其身，與朋友交言而有信。雖曰未學，吾必謂之學矣。」', '子曰：「君子不重則不威，學則不固。主忠信，無友不如己者，過則勿憚改。」', '曾子曰：「慎終追遠，民德歸厚矣。」', '子禽問於子貢曰：「夫子至於是邦也，必聞其政，求之與？抑與之與？」子貢曰：「夫子溫、良、恭、儉、讓以得之。夫子之求之也，其諸異乎人之求之與？」', '子曰：「父在，觀其志；父沒，觀其行；三年無改於父之道，可謂孝矣。」', '有子曰：「禮之用，和為貴。先王之道斯為美，小大由之。有所不行，知和而和，不以禮節之，亦不可行也。」', '有子曰：「信近於義，言可復也；恭近於禮，遠恥辱也；因不失其親，亦可宗也。」', '子曰：「君子食無求飽，居無求安，敏於事而慎於言，就有道而正焉，可謂好學也已。」', '子貢曰：「貧而無諂，富而無驕，何如？」子曰：「可也。未若貧而樂，富而好禮者也。」子貢曰：「《詩》云：『如切如磋，如琢如磨。』其斯之謂與？」子曰：「賜也，始可與言詩已矣！告諸往而知來者。」', '子曰：「不患人之不己知，患不知人也。」'], 'title': '學而'}
        assert passages == json_data

    @skip
    def test_gettextaschapterlist(self):
        '''Returns the full text of the requested URN as an object simple list of strings, each corresponding to one chapter of
text. Titles are omitted.'''
        chapters = gettextaschapterlist("ctp:analects")
        print(chapters)
        assert len(chapters) == 20   


    @skip
    def test_gettextasobject(self):
        '''Returns the full text of the requested URN as an object with a nested structure representing what each gettext API'''
        data = gettextasobject("ctp:analects/xue-er")
        print(data)
        json_data = [{'title': '學而', 'fulltext': '子曰：「學而時習之，不亦說乎？有朋自遠方來，不亦樂乎？人不知而不慍，不亦君子乎？」\n\n有子曰：「其為人也孝弟，而好犯上者，鮮矣；不好犯上，而好作亂者，未之有也。君子務本，本立而道生。孝弟也者，其為仁之本與！」\n\n子曰：「巧言令色，鮮矣仁！」\n\n曾子曰：「吾日三省吾身：為人謀而不忠乎？與朋友交而不信乎？傳不習乎？」\n\n子曰：「道千乘之國：敬事而信，節用而愛人，使民以時。」\n\n子曰：「弟子入則孝，出則弟，謹而信，汎愛眾，而親仁。行有餘力，則以學文。」\n\n子夏曰：「賢賢易色，事父母能竭其力，事君能致其身，與朋友交言而有信。雖曰未學，吾必謂之學矣。」\n\n子曰：「君子不重則不威，學則不固。主忠信，無友不如己者，過則勿憚改。」\n\n曾子曰：「慎終追遠，民德歸厚矣。」\n\n子禽問於子貢曰：「夫子至於是邦也，必聞其政，求之與？抑與之與？」子貢曰：「夫子溫、良、恭、儉、讓以得之。夫子之求之也，其諸異乎人之求之與？」\n\n子曰：「父在，觀其志；父沒，觀其行；三年無改於父之道，可謂孝矣。」\n\n有子曰：「禮之用，和為貴。先王之道斯為美，小大由之。有所不行，知和而和，不以禮節之，亦不可行也。」\n\n有子曰：「信近於義，言可復也；恭近於禮，遠恥辱也；因不失其親，亦可宗也。」\n\n子曰：「君子食無求飽，居無求安，敏於事而慎於言，就有道而正焉，可謂好學也已。」\n\n子貢曰：「貧而無諂，富而無驕，何如？」子曰：「可也。未若貧而樂，富而好禮者也。」子貢曰：「《詩》云：『如切如磋，如琢如磨。』其斯之謂與？」子曰：「賜也，始可與言詩已矣！告諸往而知來者。」\n\n子曰：「不患人之不己知，患不知人也。」\n\n'}]
        assert data == json_data

    @skip
    def test_gettextasparagraphlist(self):
        '''Returns the full text of the requested URN as a simple list of strings, each corresponding to one passage of text.
Titles are omitted.'''
        passages = gettextasparagraphlist("ctp:analects/xue-er")
        print(passages)
        json_data = [
            '子曰：「學而時習之，不亦說乎？有朋自遠方來，不亦樂乎？人不知而不慍，不亦君子乎？」', 
            '有子曰：「其為人也孝弟，而好犯上者，鮮矣；不好犯上，而好作亂者，未之有也。君子務本，本立而道生。孝弟也者，其為仁之本與！」', 
            '子曰：「巧言令色，鮮矣仁！」', '曾子曰：「吾日三省吾身：為人謀而不忠乎？與朋友交而不信乎？傳不習乎？」', '子曰：「道千乘之國：敬事而信，節用而愛人，使民以時。」', '子曰：「弟子入則孝，出則弟，謹而信，汎愛眾，而親仁。行有餘力，則以學文。」', '子夏曰：「賢賢易色，事父母能竭其力，事君能致其身，與朋友交言而有信。雖曰未學，吾必謂之學矣。」', '子曰：「君子不重則不威，學則不固。主忠信，無友不如己者，過則勿憚改。」', '曾子曰：「慎終追遠，民德歸厚矣。」', '子禽問於子貢曰：「夫子至於是邦也，必聞其政，求之與？抑與之與？」子貢曰：「夫子溫、良、恭、儉、讓以得之。夫子之求之也，其諸異乎人之求之與？」', '子曰：「父在，觀其志；父沒，觀其行；三年無改於父之道，可謂孝矣。」', '有子曰：「禮之用，和為貴。先王之道斯為美，小大由之。有所不行，知和而和，不以禮節之，亦不可行也。」', '有子曰：「信近於義，言可復也；恭近於禮，遠恥辱也；因不失其親，亦可宗也。」', '子曰：「君子食無求飽，居無求安，敏於事而慎於言，就有道而正焉，可謂好學也已。」', '子貢曰：「貧而無諂，富而無驕，何如？」子曰：「可也。未若貧而樂，富而好禮者也。」子貢曰：「《詩》云：『如切如磋，如琢如磨。』其斯之謂與？」子曰：「賜也，始可與言詩已矣！告諸往而知來者。」', '子曰：「不患人之不己知，患不知人也。」']
        assert passages == json_data

    @skip
    def test_gettextasstring(self):
        '''Returns the full text of the requested URN as a single string. Each paragraph is separated with “\n\n”.'''
        string = gettextasstring("ctp:analects/xue-er")
        print(string)
        assert False

    @skip
    def test_gettextinfo(self):
        data = gettextinfo("ctp:analects")
        print(data)
        json_data = {'dynasty': {'from': {'id': '3', 'name': 'Spring and Autumn'}, 'to': {'id': '4', 'name': 'Warring States'}}, 
                     'edition': {'collectionid': '8', 'title': '武英殿十三經注疏', 'url': 'http://ctext.org/library.pl?if=en&res=77721'}, 
                     'lastmodified': '2015-12-07 20:42:56', 
                     'tags': ['TEXTDB'], 
                     'title': '論語', 
                     'toptitle': '論語', 
                     'topurn': 
                     'ctp:analects', 
                     'workurn': 'ctp:work:analects'
                     }
        assert data == json_data

    @skip
    def test_searchtexts(self):
        data = searchtexts("論語注疏")
        print(data)
        json_data = {'books': [{'title': '論語注疏', 'urn': 'ctp:lunyu-zhushu'}, {'title': '論語注疏', 'urn': 'ctp:wb242790'}, {'title': '論語注疏', 'urn': 'ctp:wb640528'}, {'title': '論語注疏', 'urn': 'ctp:wb569805'}, {'title': '論語注疏', 'urn': 'ctp:wb714320'}, {'title': '論語注疏', 'urn': 'ctp:wb902299'}, {'title': '論語注疏解經', 'urn': 'ctp:wb195112'}]}
        assert data == json_data

    @skip
    def  test_others(self):
        setapikey("your-api-key-goes-here")
        setlanguage("zh")
        setremap("gb")

        

    


