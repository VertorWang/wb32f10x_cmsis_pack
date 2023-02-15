# -*- coding: utf-8 -*-

import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))


# 各个子系列有哪些型号
sub_family_models = [
  {
    'name': '101',
    'freq': 32000000,
    'models': ['K6', 'T6', 'C6', 'R6', 'K8', 'T8', 'C8', 'R8']
  },
  {
    'name': '102',
    'freq': 48000000,
    'models': ['K6', 'T6', 'C6', 'R6', 'K8', 'T8', 'C8', 'R8']
  },
  {
    'name': '103',
    'freq': 72000000,
    'models': ['K8', 'T8', 'T9', 'TB', 'C8', 'C9', 'CB', 'R8', 'R9', 'RB']
  },
  {
    'name': '104',
    'freq': 96000000,
    'models': ['T9', 'TB', 'TA', 'TC', 'C9', 'CB', 'CA', 'CC', 'R9', 'RB', 'RA', 'RC']
  },
  {
    'name': '105',
    'freq': 128000000,
    'models': ['T9', 'TB', 'TA', 'TC', 'C9', 'CB', 'CA', 'CC', 'R9', 'RB', 'RA', 'RC']
  },
]

all_devices_name = []
for f in sub_family_models:
  for m in f['models']:
    all_devices_name.append(f"WB32F{f['name']}{m}")


flash_sram_size_code_map = {
  '6': (32*1024, 12*1024),
  '8': (64*1024, 20*1024),
  '9': (96*1024, 28*1024),
  'B': (128*1024, 28*1024),
  'A': (192*1024, 36*1024),
  'C': (256*1024, 36*1024),
}

pin_count_code_map = {
  'K': 32,
  'T': 36,
  'C': 48,
  'R': 64,
}

out_text = ''
for f in sub_family_models:
  sub_family_devices_text = ''
  for m in f['models']:
    name = f"WB32F{f['name']}{m}"
    size = flash_sram_size_code_map[name[-1]]
    flash_size_text = f'"0x{size[0]:X}"'
    while len(flash_size_text) < 9:
      flash_size_text += ' '
    sram_size_text = f'"0x{size[1]:X}"'
    while len(sram_size_text) < 8:
      sram_size_text += ' '
    template = env.get_template('template_device.txt')
    template_out = template.render(device_name=name, device_flash_size=flash_size_text, device_sram_size=sram_size_text, device_flm_name=f'WB32F10x_{size[0]//1024}.FLM')
    template_out += '\n'
    sub_family_devices_text += template_out

  sub_family_devices_text = sub_family_devices_text.rstrip('\n')
  template = env.get_template('template_sub_family.txt')
  template_out = template.render(sub_family_name=f"WB32F{f['name']}", sub_family_freq=f['freq'], sub_family_devices=sub_family_devices_text)
  out_text += template_out

out_text = out_text.replace('\r\n', '\n')
out_text = out_text.replace('\n', '\n      ')
print(out_text)

print('Write to out_text file.')
with open('out_text', 'w') as fp:
  fp.write(out_text)

# render_dict = {
#   'sub_family_name': 'WB32F103',
#   'sub_family_devices': 'ddd'
#   }
# template_out = template.render(render_dict)
# print(template_out)
