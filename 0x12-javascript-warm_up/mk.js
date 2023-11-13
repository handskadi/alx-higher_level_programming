#!/usr/bin/node

const argc = process.argv.length;

if (argc > 2) {
	console.log('value' + (argc > 3 ? 's' : '') + ' found');
} else {
	console.log('no value');
}
