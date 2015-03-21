#!/bin/bash

mkdir fact
mkdir fact/:fact_n
mkdir fact/:fact_n/if
mkdir fact/:fact_n/if/a
mkdir 'fact/:fact_n/if/a/<='
mkdir 'fact/:fact_n/if/a/<=/a'
mkdir 'fact/:fact_n/if/a/<=/a/n'
mkdir 'fact/:fact_n/if/a/<=/b'
mkdir 'fact/:fact_n/if/a/<=/b/1'
mkdir fact/:fact_n/if/b
mkdir fact/:fact_n/if/b/1
mkdir fact/:fact_n/if/c
mkdir fact/:fact_n/if/c/*
mkdir fact/:fact_n/if/c/*/a
mkdir fact/:fact_n/if/c/*/a/n
mkdir fact/:fact_n/if/c/*/b
mkdir 'fact/:fact_n/if/c/*/b/fact()'
mkdir 'fact/:fact_n/if/c/*/b/fact()/a'
mkdir 'fact/:fact_n/if/c/*/b/fact()/a/-'
mkdir 'fact/:fact_n/if/c/*/b/fact()/a/-/a'
mkdir 'fact/:fact_n/if/c/*/b/fact()/a/-/a/n'
mkdir 'fact/:fact_n/if/c/*/b/fact()/a/-/b'
mkdir 'fact/:fact_n/if/c/*/b/fact()/a/-/b/1'
