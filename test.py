import os
import logging
import time

from biomaj_zipkin.zipkin import Zipkin

logging.basicConfig(level=logging.DEBUG)


cfg = {
    'zipkin': {
        'url': 'http://localhost:9411'
    }
}

Zipkin.set_config(cfg)

span = Zipkin('test-biomaj', 'maintrace')
span.add_binary_annotation('received something', 'blabla')

subspan = Zipkin('sub1-biomaj', 'sub1', trace_id= span.get_trace_id(), parent_id=span.get_span_id())
time.sleep(2)
subspan.trace()
subspan2 = Zipkin('sub2-biomaj', 'sub2', trace_id= span.get_trace_id(), parent_id=span.get_span_id())
time.sleep(2)
subspan2.trace()
time.sleep(1)
span.trace()
