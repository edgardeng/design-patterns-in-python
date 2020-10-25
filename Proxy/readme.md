Proxy is a structural design pattern that provides an object that acts as a substitute for a real service object used by a client. A proxy receives client requests, does some work (access control, caching, etc.) and then passes the request to a service object.

Usage examples: While the Proxy pattern isn’t a frequent guest in most Python applications, it’s still very handy in some special cases. It’s irreplaceable when you want to add some additional behaviors to an object of some existing class without changing the client code.

Identification: Proxies delegate all of the real work to some other object. Each proxy method should, in the end, refer to a service object unless the proxy is a subclass of a service.

在代理模式中，创建一个类代表另一个底层类的功能。 

保护代理用于限制访问。

虚拟代理用于对象的需时加载。
