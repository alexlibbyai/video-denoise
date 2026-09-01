// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://alexlibby.github.io',
	base: '/video-denoise',

	integrations: [
		starlight({
			title: 'Video Denoise',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/withastro/starlight' }],
			sidebar: [
			{
				label: 'Project',
				items: [
				{ label: 'Overview', slug: 'project/overview' },
				{ label: 'Roadmap', slug: 'project/roadmap' }
				]
			},

			{
				label: 'Theory',
				items: [
				{ label: 'Biological Inspiration', slug: 'theory/biology' },
				{ label: 'Neuron Model', slug: 'theory/neuron-model' },
				{ label: 'RMS Encoding', slug: 'theory/encoder' },
				{ label: 'Reservoir Design', slug: 'theory/reservoir' },
				{ label: 'Learning Mechanisms', slug: 'theory/learning' }
				]
			},

			{
				label: 'Architecture',
				items: [
				{
					label: 'System Overview',
					slug: 'architecture/system-overview'
				}
				]
			},

			{
				label: 'Experiments',
				items: [
				{
					label: 'Experiment Log',
					slug: 'experiments/experiment-log'
				}
				]
			},

			{
				label: 'Results',
				items: [
				{
					label: 'Results',
					slug: 'results/results-log'
				}
				]
			}
			],
		}),
	],
});
