import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.videos import Videos


class VideosServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.videos = Videos(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "videos": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.list(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "bucketId": "5e5ea5c16897e",
            "fileId": "d5fg5ehg1c168g7c",
            "name": "Product demo",
            "size": 23647142.0,
            "format": "MPEG-4",
            "duration": 92810.0,
            "width": 960.0,
            "height": 544.0,
            "aspectRatio": "16:9",
            "videoCodec": "h264",
            "videoFormat": "AVC",
            "videoFormatProfile": "Baseline@L3.1",
            "videoBitRate": 564790.0,
            "videoFrameRate": 29.97,
            "videoFrameRateMode": "CFR",
            "audioCodec": "aac",
            "audioFormat": "AAC",
            "audioBitRate": 127999.0,
            "audioSampleRate": 48000.0,
            "timelineStatus": "ready",
            "timelineError": "The requested file is not a valid video or audio file (ffprobe: Invalid data found when processing input)",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.create(
            '<VIDEO_ID>',
            '<BUCKET_ID>',
            '<FILE_ID>',
            name='<NAME>',
            permissions=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'videoId': '<VIDEO_ID>',
                'bucketId': '<BUCKET_ID>',
                'fileId': '<FILE_ID>',
                'name': '<NAME>',
                'permissions': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_codecs(self, m):
        data = {
            "total": 5.0,
            "codecs": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.list_codecs()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/codecs',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "bucketId": "5e5ea5c16897e",
            "fileId": "d5fg5ehg1c168g7c",
            "name": "Product demo",
            "size": 23647142.0,
            "format": "MPEG-4",
            "duration": 92810.0,
            "width": 960.0,
            "height": 544.0,
            "aspectRatio": "16:9",
            "videoCodec": "h264",
            "videoFormat": "AVC",
            "videoFormatProfile": "Baseline@L3.1",
            "videoBitRate": 564790.0,
            "videoFrameRate": 29.97,
            "videoFrameRateMode": "CFR",
            "audioCodec": "aac",
            "audioFormat": "AAC",
            "audioBitRate": 127999.0,
            "audioSampleRate": 48000.0,
            "timelineStatus": "ready",
            "timelineError": "The requested file is not a valid video or audio file (ffprobe: Invalid data found when processing input)",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.get(
            '<VIDEO_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "bucketId": "5e5ea5c16897e",
            "fileId": "d5fg5ehg1c168g7c",
            "name": "Product demo",
            "size": 23647142.0,
            "format": "MPEG-4",
            "duration": 92810.0,
            "width": 960.0,
            "height": 544.0,
            "aspectRatio": "16:9",
            "videoCodec": "h264",
            "videoFormat": "AVC",
            "videoFormatProfile": "Baseline@L3.1",
            "videoBitRate": 564790.0,
            "videoFrameRate": 29.97,
            "videoFrameRateMode": "CFR",
            "audioCodec": "aac",
            "audioFormat": "AAC",
            "audioBitRate": 127999.0,
            "audioSampleRate": 48000.0,
            "timelineStatus": "ready",
            "timelineError": "The requested file is not a valid video or audio file (ffprobe: Invalid data found when processing input)",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.update(
            '<VIDEO_ID>',
            name='<NAME>',
            permissions=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'permissions': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.delete(
            '<VIDEO_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_captions(self, m):
        data = {
            "total": 5.0,
            "captions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.list_captions(
            '<VIDEO_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/captions',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_caption(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "videoId": "5e5ea5c16897e",
            "bucketId": "d5fg5ehg1c168g7c",
            "fileId": "c5fg5emg1c168grr",
            "name": "English",
            "language": "eng",
            "default": True,
            "embedded": True,
            "targetDuration": 93,
            "status": "ready",
            "error": "Caption is not a proper .srt file (Invalid timestamp delimiter at line 2)",
            "size": 4096.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.create_caption(
            '<VIDEO_ID>',
            '<BUCKET_ID>',
            '<FILE_ID>',
            '<NAME>',
            'aar',
            default=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/captions',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'bucketId': '<BUCKET_ID>',
                'fileId': '<FILE_ID>',
                'name': '<NAME>',
                'language': 'aar',
                'default': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_caption(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "videoId": "5e5ea5c16897e",
            "bucketId": "d5fg5ehg1c168g7c",
            "fileId": "c5fg5emg1c168grr",
            "name": "English",
            "language": "eng",
            "default": True,
            "embedded": True,
            "targetDuration": 93,
            "status": "ready",
            "error": "Caption is not a proper .srt file (Invalid timestamp delimiter at line 2)",
            "size": 4096.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.update_caption(
            '<VIDEO_ID>',
            '<CAPTION_ID>',
            bucket_id='<BUCKET_ID>',
            file_id='<FILE_ID>',
            name='<NAME>',
            language='aar',
            default=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/captions/<CAPTION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'bucketId': '<BUCKET_ID>',
                'fileId': '<FILE_ID>',
                'name': '<NAME>',
                'language': 'aar',
                'default': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_caption(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.delete_caption(
            '<VIDEO_ID>',
            '<CAPTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/captions/<CAPTION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_cmaf_hls_manifest(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.videos.get_cmaf_hls_manifest(
            '<VIDEO_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/outputs/cmaf/master.m3u8',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_cmaf_dash_manifest(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.videos.get_cmaf_dash_manifest(
            '<VIDEO_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/outputs/cmaf/master.mpd',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_dash_manifest(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.videos.get_dash_manifest(
            '<VIDEO_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/outputs/dash/master.mpd',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_hls_manifest(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.videos.get_hls_manifest(
            '<VIDEO_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/outputs/hls/master.m3u8',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_caption_manifest(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.videos.get_caption_manifest(
            '<VIDEO_ID>',
            'hls',
            '<CAPTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/outputs/hls/captions/<CAPTION_ID>/manifest',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_renditions(self, m):
        data = {
            "total": 5.0,
            "renditions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.list_renditions(
            '<VIDEO_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/renditions',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_rendition(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "videoId": "5e5ea5c16897e",
            "profileId": "d5fg5ehg1c168g7c",
            "name": "1280X720@3679",
            "startedAt": "2020-10-15T06:38:00.000+00:00",
            "endedAt": "2020-10-15T06:38:00.000+00:00",
            "width": 1280.0,
            "height": 720.0,
            "videoBitRate": 3551000.0,
            "audioBitRate": 128000.0,
            "targetDuration": 6.006,
            "status": "ready",
            "error": "The requested file is not a valid video or audio file (ffprobe: Invalid data found when processing input)",
            "progress": 88.0,
            "output": "hls",
            "codec": "h264",
            "size": 18350080.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.create_rendition(
            '<VIDEO_ID>',
            '<PROFILE_ID>',
            'hls',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/renditions',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'profileId': '<PROFILE_ID>',
                'output': 'hls',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_rendition(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "videoId": "5e5ea5c16897e",
            "profileId": "d5fg5ehg1c168g7c",
            "name": "1280X720@3679",
            "startedAt": "2020-10-15T06:38:00.000+00:00",
            "endedAt": "2020-10-15T06:38:00.000+00:00",
            "width": 1280.0,
            "height": 720.0,
            "videoBitRate": 3551000.0,
            "audioBitRate": 128000.0,
            "targetDuration": 6.006,
            "status": "ready",
            "error": "The requested file is not a valid video or audio file (ffprobe: Invalid data found when processing input)",
            "progress": 88.0,
            "output": "hls",
            "codec": "h264",
            "size": 18350080.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.get_rendition(
            '<VIDEO_ID>',
            '<RENDITION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/renditions/<RENDITION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_rendition(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.videos.delete_rendition(
            '<VIDEO_ID>',
            '<RENDITION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/renditions/<RENDITION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_thumbnail(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.videos.get_thumbnail(
            '<VIDEO_ID>',
            '<THUMBNAIL_ID>',
            width=1,
            height=1,
            output='jpg',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/thumbnails/<THUMBNAIL_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'width': ['1'],
                'height': ['1'],
                'output': ['jpg'],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_timeline(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.videos.get_timeline(
            '<VIDEO_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/videos/<VIDEO_ID>/timeline',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response, data)
