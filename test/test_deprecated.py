import asyncio
import unittest
import warnings

from appwrite.utils.deprecated import deprecated


class TestDeprecatedDecorator(unittest.IsolatedAsyncioTestCase):

    def test_warns_on_every_call(self):
        @deprecated("use new_api instead")
        def old_api():
            return 'ok'

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always', DeprecationWarning)
            self.assertEqual('ok', old_api())
            self.assertEqual('ok', old_api())

        self.assertEqual(
            [
                "Call to deprecated function 'old_api'. use new_api instead",
                "Call to deprecated function 'old_api'. use new_api instead",
            ],
            [str(warning.message) for warning in caught],
        )

    def test_warning_is_attributed_to_the_caller(self):
        @deprecated("use new_api instead")
        def old_api():
            return 'ok'

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always', DeprecationWarning)
            old_api()

        self.assertEqual(__file__, caught[0].filename)

    def test_caller_filters_are_restored(self):
        @deprecated("use new_api instead")
        def old_api():
            return 'ok'

        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            before = warnings.filters[:]
            old_api()
            after = warnings.filters[:]

        self.assertEqual(before, after)

    def test_caller_filters_still_apply_after_the_call(self):
        @deprecated("use new_api instead")
        def old_api():
            return 'ok'

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('ignore', DeprecationWarning)
            old_api()
            warnings.warn('unrelated', DeprecationWarning)

        self.assertEqual(
            ["Call to deprecated function 'old_api'. use new_api instead"],
            [str(warning.message) for warning in caught],
        )

    async def test_async_warning_is_attributed_to_the_caller(self):
        @deprecated("use new_api instead")
        async def old_api():
            return 'ok'

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always', DeprecationWarning)
            await old_api()

        self.assertEqual(__file__, caught[0].filename)

    async def test_awaited_call_is_not_affected_by_the_temporary_filter(self):
        @deprecated("use new_api instead")
        async def old_api():
            warnings.warn('unrelated', DeprecationWarning)
            await asyncio.sleep(0)
            warnings.warn('unrelated after await', DeprecationWarning)
            return 'ok'

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('ignore', DeprecationWarning)
            result = await old_api()

        self.assertEqual('ok', result)
        self.assertEqual(
            ["Call to deprecated function 'old_api'. use new_api instead"],
            [str(warning.message) for warning in caught],
        )

    async def test_awaited_call_runs_without_the_always_filter(self):
        observed = []

        @deprecated("use new_api instead")
        async def old_api():
            observed.extend(
                (action, category)
                for action, message, category, module, lineno in warnings.filters
                if category is DeprecationWarning
            )
            return 'ok'

        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            await old_api()

        self.assertNotIn(('always', DeprecationWarning), observed)

    async def test_async_caller_filters_are_restored(self):
        @deprecated("use new_api instead")
        async def old_api():
            return 'ok'

        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            before = warnings.filters[:]
            await old_api()
            after = warnings.filters[:]

        self.assertEqual(before, after)
