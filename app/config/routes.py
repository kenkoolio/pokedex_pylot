
from system.core.router import routes

routes['default_controller'] = 'Welcome'
routes['/'] = 'Welcome#index'
