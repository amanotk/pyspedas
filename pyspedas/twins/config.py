import os

CONFIG = {'local_data_dir': 'twins_data/',
          'remote_data_dir': 'https://spdf.sci.gsfc.nasa.gov/pub/data/twins/'}

# override local data directory with environment variables
if os.environ.get('ROOT_DATA_DIR'):
    CONFIG['local_data_dir'] = os.sep.join([os.environ['ROOT_DATA_DIR'], 'twins'])

if os.environ.get('TWINS_DATA_DIR'):
    CONFIG['local_data_dir'] = os.environ['TWINS_DATA_DIR']