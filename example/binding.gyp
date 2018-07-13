{
  "targets": [{
    "target_name": "pat",
    "include_dirs": [
      "<!(node -e \"require('napi-macros')\")"
    ],
    "sources": [
      "./binding.c"
    ],
    "xcode_settings": {
      "OTHER_CFLAGS": [
        "-O3",
        "-std=c99",
        "-D_GNU_SOURCE"
      ]
    },
    "cflags": [
      "-O3",
      "-std=c99",
      "-D_GNU_SOURCE"
    ],
  }]
}

