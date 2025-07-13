from django_redis import get_redis_connection
import logging
from django.core.cache import cache
from properties.models import Property



def getallproperties():
    all_properties = cache.get('all_properties')
    if all_properties is None:
        all_properties = list(Property.objects.all())
        cache.set('all_properties', all_properties, 3600)
    return all_properties



logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    redis_conn = get_redis_connection("default")
    info = redis_conn.info()

    keyspace_hits = info.get("keyspace_hits", 0)
    keyspace_misses = info.get("keyspace_misses", 0)
    total_requests = keyspace_hits + keyspace_misses

    hit_ratio = keyspace_hits / total_requests if total_requests > 0 else 0 

    metrics = {
        "hits": keyspace_hits,
        "misses": keyspace_misses,
        "hit_ratio": round(hit_ratio, 3)
    }

    logger.error(f"Redis Cache Metrics: {metrics}")
    return metrics