import zlib
import binascii

data = b'Hello worldHello worldHello worldHello'

#Compression
compress = zlib.compressobj(zlib.Z_BEST_COMPRESSION, zlib.DEFLATED, +15)
compressed_data = compress.compress(data)
compress_ratio = (float(len(data)) - float(len(compressed_data))) / float(len(data))
compressed_data += compress.flush()

print('Original:          ',  data)
print('Compressed data:   ',  binascii.hexlify(compressed_data))
print('Compressed:         %d%%' % (100.0 * compress_ratio))

#Decompressor
decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(compressed_data)
print('De-Compressed data:', decompressed)
decompressed += decompressor.flush()
