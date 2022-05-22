import logging.config
import sys
from lru_cache import LRUCache


if __name__ == '__main__':
    log_config = {
        "version": 1,
        "formatters": {
            "simple": {
                "format": "%(levelname)s\t%(processName)s\t%(message)s",
            },
            "dated": {
                "format": "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s",
            },
        },
        "handlers": {
            "cache_file": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "filename": "cache.log",
                "formatter": "dated",
            },
            "system": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
                "formatter": "simple",
            },
        },
        "loggers": {
            "output": {
                "level": "INFO",
                "handlers": ["system"],
            },
            "cache": {
                "level": "ERROR",
                "handlers": ["cache_file"],
            },
        },
    }
    logging.config.dictConfig(log_config)

    cache_logger = logging.getLogger('cache')
    if '-s' in sys.argv:
        output_logger = logging.getLogger('output')
    else:
        output_logger = logging.getLogger('dummy')

    lru_cache = LRUCache(10)
    output_logger.info('LRU_Cache_created')

    for i in range(5):
        lru_cache.set(f'k{i+1}', f'val{i+1}')
        output_logger.info('k%i_set', i+1)
    output_logger.info('completed_filling')

    for i in range(7):
        test = lru_cache.get(f'k{i+1}')
        if test is None:
            cache_logger.error('cant_get_element_k%i', i+1)
        else:
            output_logger.info('successfully_received_item_k%i', i+1)

    if lru_cache.get('k1') is not None:
        lru_cache.set('k1', 'val1')
        output_logger.info('successfully_overwritten_item_k1')

    if lru_cache.get('test') is None:
        cache_logger.error('cant_get_item_test')
